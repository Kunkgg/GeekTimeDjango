from datetime import datetime
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

JobTypes = (
    (0, '开发'),
    (1, '运维'),
    (2, '设计'),
    (3, '测试'),
    (4, '管理'),
)

Cities = (
    (0, '北京'),
    (1, '上海'),
    (2, '广州'),
    (3, '深圳'),
    (4, '西安'),
    (5, '成都'),
    (6, '杭州'),
    (7, '南京'),
)


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
    job_type = models.SmallIntegerField(choices=JobTypes, blank=False, verbose_name='职位类别')
    job_name = models.CharField(max_length=32, blank=False, verbose_name='职位名称')
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name='工作城市')
    job_responsibility = models.TextField(max_length=1024, verbose_name='职位职责')
    job_requirement = models.TextField(max_length=1024, verbose_name='职位要求')
    creator = models.ForeignKey(User, null=True, verbose_name='创建人', on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name='创建时间', default=datetime.now)


