from datetime import datetime
from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# 候选人学历
DEGREE_TYPE = (('本科', '本科'), ('硕士', '硕士'), ('博士', '博士'))


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

class Resume(models.Model):
    # Translators: 简历实体的翻译
    username = models.CharField(max_length=255, verbose_name=_('姓名'))
    applicant = models.ForeignKey(User, verbose_name=_('申请人'), null=True, on_delete=models.SET_NULL)
    city = models.CharField(max_length=255, verbose_name=_('城市'))
    phone = models.CharField(max_length=255, verbose_name=_('手机号码'))
    email = models.EmailField(max_length=255, blank=True, verbose_name=_('邮箱'))
    apply_position = models.CharField(max_length=255, blank=True, verbose_name=_('应聘职位'))
    born_address = models.CharField(max_length=255, blank=True, verbose_name=_('生源地'))
    gender = models.CharField(max_length=255, blank=True, verbose_name=_('性别'))
    # picture = models.ImageField(upload_to='images/', blank=True, verbose_name=_('个人照片')) 
    # attachment = models.FileField(upload_to='files/', blank=True, verbose_name=_('简历附件'))

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=255, blank=True, verbose_name=_('本科学校'))
    master_school = models.CharField(max_length=255, blank=True, verbose_name=_('研究生学校'))
    doctor_school = models.CharField(max_length=255, blank=True, verbose_name=_('博士生学校'))
    major = models.CharField(max_length=255, blank=True, verbose_name=_('专业'))
    degree = models.CharField(max_length=255, choices=DEGREE_TYPE, blank=True, verbose_name=_('学历'))
    created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改日期", auto_now=True)

    # 候选人自我介绍，工作经历，项目经历
    candidate_introduction = models.TextField(max_length=1024, blank=True, verbose_name=_('自我介绍'))
    work_experience = models.TextField(max_length=1024, blank=True, verbose_name=_('工作经历'))
    project_experience = models.TextField(max_length=1024, blank=True, verbose_name=_('项目经历'))

    class Meta:
        verbose_name = _('简历')
        verbose_name_plural = _('简历列表')
        ordering = ('-created_date',)
    
    def __str__(self):
        return self.username
