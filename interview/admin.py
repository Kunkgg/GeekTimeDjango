from datetime import datetime
import csv
from django.contrib import admin
from django.http import HttpResponse


from .models import Candidate


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

class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date', 'last_editor')

    list_display = (
    'username', 'city', 'bachelor_school', 'test_score_of_general_ability', 'paper_score', 'first_score', 'first_result', 'first_interviewer_user', 'second_score',
    'second_result', 'second_interviewer_user', 'hr_score', 'hr_result', 'hr_interviewer_user',)

    search_fields = ('username', 'city', 'bachelor_school', 'phone', 'email')

    list_filter = ('city', 'gender')

    ordering = ('test_score_of_general_ability', 'paper_score')

    actions = (export_model_as_csv,)

    fieldsets = (
        ('基础信息', {
            'description': '面试人员基本信息',
            'fields': (
                "userid",
                ("username",  "city", "phone"),
                ("gender", "born_address"),
                ("apply_position", "email"),
                "candidate_remark",
            )
        }),
        ('学校与学历信息', {
            'fields': (
                "bachelor_school",
                "master_school",
                "doctor_school",
                "major",
                "degree",
            )
        }),
        ('综合能力测评成绩，笔试测评成绩', {
            'fields': (
                "test_score_of_general_ability",
                "paper_score",
            )
        }),
        ('第一轮面试记录', {
            'fields': (
                "first_score",
                "first_learning_ability",
                "first_professional_competency",
                "first_advantage",
                "first_disadvantage",
                "first_result",
                "first_recommend_position",
                "first_interviewer_user",
                "first_remark",
            )
        }),
        ('第二轮面试记录', {
            'classes': ('extrapretty',),
            'fields': (
                "second_score",
                "second_learning_ability",
                "second_professional_competency",
                "second_pursue_of_excellence",
                "second_communication_ability",
                "second_pressure_score",
                "second_advantage",
                "second_disadvantage",
                "second_result",
                "second_recommend_position",
                "second_interviewer_user",
                "second_remark",
            )
        }),
        ('HR终面', {
            'classes': ('collapse', 'extrapretty'),
            'fields': (
                "hr_score",
                "hr_responsibility",
                "hr_communication_ability",
                "hr_logic_ability",
                "hr_potential",
                "hr_stability",
                "hr_advantage",
                "hr_disadvantage",
                "hr_result",
                "hr_interviewer_user",
                "hr_remark",
            )
        })
    )

admin.site.register(Candidate, CandidateAdmin)
