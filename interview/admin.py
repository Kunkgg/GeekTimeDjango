from datetime import datetime
import csv
import logging


from django.contrib import admin
from django.http import HttpResponse
from django.db.models import Q


from .models import Candidate
from .candidate_fieldsets import basic_fieldsets
from .candidate_fieldsets import first_interviewer_fieldsets
from .candidate_fieldsets import second_interviewer_fieldsets
from .candidate_fieldsets import hr_interviewer_fieldsets

LOG = logging.getLogger()


# 导出为 csv 文件
def export_model_as_csv(modeladmin, request, queryset):
    field_list = (
        'username',
        'city',
        'phone',
        'bachelor_school',
        'major',
        'degree',
        'test_score_of_general_ability',
        'paper_score',
    )
    response = HttpResponse(content_type='text/csv')
    model_name = modeladmin.model._meta.model_name
    time_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'{model_name}_list_{time_str}.csv'
    response['Content-Disposition'] = f'attachment;filename={filename}'

    # 写入表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list],
    )
    # for obj in queryset:
    #     ## 单行 的记录（各个字段的值）， 根据字段对象，从当前实例 (obj) 中获取字段值
    #     csv_line_values = []
    #     for field in field_list:
    #         field_object = queryset.model._meta.get_field(field)
    #         field_value = field_object.value_from_object(obj)
    #         csv_line_values.append(field_value)
    #     writer.writerow(csv_line_values)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_list])

    return response

export_model_as_csv.short_description = '导出为 CSV 文件'
export_model_as_csv.allowed_permissions = ('export',)

class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date', 'last_editor')

    list_display = (
    'username', 'city', 'bachelor_school', 'test_score_of_general_ability',
    'paper_score', 'first_score', 'first_result', 'first_interviewer_user', 'second_score',
    'second_result', 'second_interviewer_user', 'hr_score', 'hr_result', 'hr_interviewer_user',)

    search_fields = ('username', 'city', 'bachelor_school', 'phone', 'email')

    list_filter = ('city', 'gender')

    ordering = ('test_score_of_general_ability', 'paper_score')

    actions = (export_model_as_csv,)

    def has_export_permission(self, request):
        return request.user.has_perm(f'{self.opts.app_label}.export')

    # fieldsets = hr_interviewer_fieldsets

    def get_fieldsets(self, request, obj):
        rv = basic_fieldsets
        group_names = self.get_group_names(request.user)
        if request.user.username == 'admin' or 'HR' in group_names:
            rv = hr_interviewer_fieldsets
        elif 'Interviewer' in group_names:
            if request.user == obj.first_interviewer_user:
                rv = first_interviewer_fieldsets
            elif request.user == obj.second_interviewer_user:
                rv = second_interviewer_fieldsets
        return rv

    # readonly_fields = ('first_interviewer_user', 'second_interviewer_user', 'hr_interviewer_user')

    def get_group_names(self, user):
        return [group.name for group in user.groups.all()]

    def get_readonly_fields(self, request, obj):
        group_names = self.get_group_names(request.user)
        LOG.info(f"user:{request.user.username}, group_names: {group_names}")

        if request.user.username == 'admin' or 'HR' in group_names:
            return ()
        else:
            return ('first_interviewer_user', 'second_interviewer_user', 'hr_interviewer_user')

    def get_queryset(self, request):
        rv = Candidate.objects.none()
        qs = super().get_queryset(request)
        group_names = self.get_group_names(request.user)

        if request.user.is_superuser or 'HR' in group_names:
            rv = qs
        elif 'Interviewer' in group_names:
            rv = Candidate.objects.filter(Q(first_interviewer_user=request.user) | Q(second_interviewer_user=request.user))

        return rv


admin.site.register(Candidate, CandidateAdmin)
