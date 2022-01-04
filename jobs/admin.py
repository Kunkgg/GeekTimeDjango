from django.contrib import admin
from .models import Job, Resume

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

    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)

admin.site.register(Job, JobAdmin)
admin.site.register(Resume, ResumeAdmin)

