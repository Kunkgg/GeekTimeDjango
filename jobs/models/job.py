from datetime import datetime
from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from jobs.models.choices_constant import JobTypes, Cities

# 岗位信息对象：

# -   职位类别
# -   职位名称
# -   工作地点
# -   职位职责
# -   职位要求
# -   创建人
# -   创建日期
# -   修改日期

class Job(models.Model):
    job_type = models.SmallIntegerField(choices=JobTypes, blank=False, verbose_name=_('职位类别'))
    job_name = models.CharField(max_length=32, blank=False, verbose_name=_('职位名称'))
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name=_('工作城市'))
    job_responsibility = models.TextField(max_length=1024, verbose_name=_('职位职责'))
    job_requirement = models.TextField(max_length=1024, verbose_name=_('职位要求'))
    creator = models.ForeignKey(User, null=True, verbose_name=_('创建人'), on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name=_('创建时间'), default=datetime.now)
    modified_date = models.DateTimeField(verbose_name=_('修改时间'), default=datetime.now)

    class Meta:
        verbose_name = _('职位')
        verbose_name_plural = _('职位列表')
