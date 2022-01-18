from datetime import datetime

from django.contrib import admin
from django.contrib import messages

from .models import Job, Resume
from interview.models import Candidate

class JobAdmin(admin.ModelAdmin):
    exclude = (
        'creator',
        'created_date',
        'modified_date',
    )
    list_display = (
        'job_name',
        'job_type',
        'job_city',
        'creator',
        'created_date',
        'modified_date',
        )

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

def enter_interview_process(modeladmin, request, queryset):
    candidate_names = ""
    for resume in queryset:
        candidate = Candidate()
        # 把 obj 对象中的所有属性拷贝到 candidate 对象中:
        candidate.__dict__.update(resume.__dict__)
        candidate.created_date = datetime.now()
        candidate.modified_date = datetime.now()
        candidate_names = f'{candidate.username}, {candidate_names}'
        candidate.creator = request.user.username
        candidate.save()
    messages.add_message(request, messages.INFO, f'候选人: {candidate_names} 已成功进入面试流程')

enter_interview_process.short_description = "进入面试流程"


class ResumeAdmin(admin.ModelAdmin):
    exclude = (
        'applicant',
        'created_date',
        'modified_date',
    )
    list_display = (
        'username',
        'applicant',
        'apply_position',
        'city',
        'gender',
        'bachelor_school',
        'master_school',
        'doctor_school',
        'major',
        'degree',
        'created_date',
        'modified_date',
        )
    actions = (enter_interview_process,)

    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)

admin.site.register(Job, JobAdmin)
admin.site.register(Resume, ResumeAdmin)
