# Django
## 开始项目 

```
django-admin startproject <procject_name> [.]

python manage.py startapp <app_name>

python manage.py makemigrations

python manage.py migrate

python manage.py runserver [--settings path.to.settings_module] [host_ip:port]
```

## 实现岗位信息基础功能

### 添加第一个数据模型 Job 

岗位信息对象：

-   职位类别
-   职位名称
-   工作地点
-   职位职责
-   职位要求
-   创建人
-   创建日期
-   修改日期

### 定制 Job Admin

1. `list_display` 定义在 admin 列表页面显示的属性列表
1. `exclude` 定义在 admin 编辑页面隐藏的属性列表

### 匿名用户浏览职位列表及职位详情页面

1. app 模版路径: `app_dir/templates/app_dir`
1. 定义视图函数
1. 定义 URLconf
-   `path` 和 `re_path`
-   参数捕获
    -   尖括号
    -   正则表达式: `(?P<name>pattern)`
-   converter:
    -   int
    -   str
    -   path
    -   uuid
    -   slug
    -   自定义
-   `name` 建议为每条映射配置一个标识
    -   `appname-urlname`
1. include
1. reverse
    -   需要映射有 `name`
    -   在模版中使用 `url` 标签
    -   在 Python 代码中使用 `reverse` 函数
1. namespace

## 数据建模的 10 大设计原则

1. 命名清晰，无歧义
1. 一表一用
1. 不使用带有物理意义的字段作为主键
1. 完整性，数据信息完整
1. 可追溯，创建时间、修改时间, 可以逻辑删除
1. 一致性，相同的数据存储在同一张表
1. 不使用 `join` 操作查询
1. 冷热分离，冷数据和热数据分离
1. 长短分离，长文本和短文本分离，长文本独立存储
1. 索引完备

## 创建 Interview app

1. Candidate 数据模型
1. admin 列表页面信息定制、编辑页面分组展示

### Django 命令行工具，候选人数据批量导入

1. 批量导入 `csv` 格式候选人数据
2. fake_candidate 命令行工具

### Admin 筛选器、排序、搜索

1. ModelAdmin.list_filter
1. ModelAdmin.ordering
1. ModelAdmin.search_fields

### LDAP 登录

1. https://github.com/etianen/django-python3-ldap
1. 批量导入帐号 `./manage.py ldap_sync_users`
1. 为指定帐号设置超级用户权限 `./manage.py ldap_promote <username>`

### 导出 Candidate 为 csv 文件

1. 定义 admin action 导出数据
1. 参考 [](https://stackoverflow.com/questions/18685223/how-to-export-django-model-data-into-csv-file)

### 简单的 model 外键引用

1. model 的之间的关系其实就是数据库数据模型之间的关系， 包含三种
    - 一对多关系
    - 多对一关系
    - 一对一关系
    - 多对多关系
1. 这里以为候选人设置面试关为例， 演示多对一关系， 多个候选人可以对应同一个面试官
1. 面试官使用 `django.contrib.auth.models.User`

### 设置 admin 只读字段

1. ModelAdmin.readonly_fields 属性， 指定 read_only 序列
1. ModelAdmin.get_readonly_fields(request, obj=None) 方法， 添加只读字段的逻辑，
比如仅当当前用户为 admin 或 HR 用户组成员时开放面试官字段的编辑权限，其他用户对面试官只读
### 更灵活的方式设置 admin fieldsets

1. get_fieldsets(self, request, obj) 方法
1. 第一二轮面试官仅允许便是其相应的范围

### admin get_queryset

1. 覆盖 `get_queryset(self, request)` 方法，
实现面试官仅可以浏览分配到自己的候选人列表

### 自定义权限

1. 定义候选人信息导出权限
1. 在 `class Meta` 中定义 `permissions`
1. 编辑对应 action 函数的 `allowed_permissions` 属性
1. 定义 admin class 中的 `has_XX_permission(self, reuqest)` 方法
## 简历投递功能
### 集成注册登录功能

1. [django-registration-redux](https://github.com/macropin/django-registration) 支持三种方式
    - 用户激活邮件两步认证
    - 管理员激活邮件两步认证
    - 简单直无需激活一步认证
1. 支持第三方认证 [django-allauth](https://www.intenct.nl/projects/django-allauth/)

### 编辑模版显示用户登录状态

1. 在 `base.html` 增加 `nav` 元素，显示用户登录状态

### 增加简历数据模型

### 用户投递简历

1. 已注册的用户可以在岗位详情页面点击 `提交申请` 按钮，提交简历
1. 简历与当前用户关联
1. 使用通用视图 `CreateView`

### 安排简历进入面试环节

1. 实际就是根据 Resume 对象在 Candidate 表里创建相应的候选人对象
1. Resume admin 增加 `enter_interview_process` action
1. 使用 Django message

### 用户简历详情页面

1. 使用通用视图 `DetailView` 展示用户简历详情页面

### 自定义 admin 列表字段

1. 为 admin Candidate(应聘者) 列表页面增加一个字段，用于显示候选人原始简历链接

## 完善项目
### 如何使用日志

1. 在 `settings.py` 中定义 `LOGGING` 变量, 
它是一个标准库 logging 模块的 dictConfig 字典。

### 生产环境与开发环境配置分离

1. 生产环境与开发环境配置注意区别
    - 生产环境一般不允许有 DEBUG 信息
    - 生产环境不允许有密钥、证书等敏感信息
    - 生产环境和开发环境可能使用不同的数据库
1. 通过 `DJANGO_SETTINGS_MODULE` 环境变量指定配置模块路径，
默认路径为 `project_name.settings`, 可在 `manage.py` 中修改。
当既没有从命令行指定 `manage.py runserver --settings=settings.local`,
也没有设置环境变量 `DJANGO_SETTINGS_MODULE` 时默认配置会才会生效。
1. 配置文件优先级顺序
    1. 命令行指定
    1. 环境变量指定
    1. 默认值

### 自定义 admin 站点的 header 和 title

1. 在项目 `urls.py` 中设置 `admin.site.site_header` 和 `admin.site.site_title`
1. admin 站点其他属性参考 https://docs.djangoproject.com/en/4.0/ref/contrib/admin/
1. 尝试了在项目 app 目录下新建 `admin.py` 文件中设置， 但结果不能生效。
说明 django 可能不会像处理其他 `startapp` 创建的目录中的 `admin.py` 一样处理项目 app 目录下的 `admin.py`。 

### 替换 admin 默认主题

1. 安装主题包
1. 添加进 `INSTALLED_APPS`
1. 配置 `urls.py`
1. 注意， `django-grappelli==2.15.3` 在 Django 3 中使用会报错。[resolved-issue](https://github.com/sehmaschine/django-grappelli/issues/978)
1. [Github django-grappelli](https://github.com/sehmaschine/django-grappelli)

### 使用 CSS 框架定制页面

1. [django-bootstrap](https://github.com/zelenij/django-bootstrap-v5)
    - 注意， 在使用 messages 的时候需要同时 `load bootstrap5` 和 `load i18n`
1. [django-bulma](https://github.com/timonweb/django-bulma)
1. [django-tailwind](https://github.com/timonweb/django-tailwind)

## 使用 inspectdb 和 多数据库路由为已有数据库生成管理后台

1. 在 settings 中增加数据库配置
1. 新建 app 用于管理已有数据库
1. `inspectdb` 生成已有数据库的 `models.py`
    ```
    python manage.py inspectdb --settings=settings.local --database=toy > models.py
    ```
1. 在 settings 中通过 `DATABASE_ROUTERS` 引入多数据库路由

## 自定义中间件

1. 什么是中间件？
    - 注入在请求/响应流程中的钩子框架，可以对 request/response 做自定义的处理
1. 常见应用场景
    - 登录认证，安全拦截
    - 日记记录，性能分析
    - 缓存处理，告警监控

### 自定义性能日志中间件 performance_logger_middleware

1. 定义函数 `performance_logger_middleware(get_response)`

## 多语言支持

1. 使用 gettext 或者 gettext_lazy 方法标记需要多语言支持的字符串
1. 在 settings 修改语言相关的配置
1. 在 settings 中增加中间件 `django.middleware.locale.LocaleMiddleware`,
注意，该中间的顺序，在 `SessionMiddleware` 之后, 
`CacheMiddleware` 和 `CommonMiddleware` 之前。
1. 在模版中使用 `{% load i18n %}` 和 `translate`, `blocktranslate` 等标签
1. 使用命令工具生成和编译 locale 文件
    ```
    python manage.py makemessages -l zh_HANS -l en
    python manage.py compliemessages
    ```
1. 未解决问题：**部分** zh-HANS 翻译文本无法生效

## 集成 Sentry

1. 使用 docker-compose 部署 [Sentry-self-hosted](https://github.com/getsentry/self-hosted)
1. 安装 `pip install sentry-sdk`
1. 在 settings 中加入 sentry 初始化配置

### 定义 Sentry 异常捕获和性能监控中间件

1. 当处理请求时间大于 `SLOW_MS` 时，认为时慢查询，使用 `capture_message` 上报
1. 当处理请求过程中发生异常时， 使用 `capture_exception` 上报

## 安全防护
### 防止 XSS 

- 攻击者在提交的表单中注入脚本
- 防止方式: 不直接返回未经转义的 html

### 防止 CSRF

- 攻击者建立伪装网站，在用户不知情的情况下利用表单绕过浏览器跨域限制，
进而利用浏览器中的 cookie 实施攻击。
- 防止方式: 在提交表单时使用 `csrf_token`

## Django Rest Framework (DRF)

- https://www.django-rest-framework.org/
- api url: http://localhost:8000/api/
- 开放 Job， User, Candidate, Resume 模型的 api

### api 权限设置

- Job 权限
    - `superuser` 和 `HR` 组成员可以编辑
    - 未登录用户及其他用户只读
    - `Job.creator`, `Job.created_date` 和 `Job.modified_date` 属性始终只读
- User 权限
    - 未登录用户无权限
    - `superuser` 可编辑
    - 其他登录用户仅允许编辑自己的 `User.email` 属性，其他属性只读
    - 注意：直接使用 `django.contrib.auth.User` 可能导致无法控制权限, 
    建议在所有 django 项目开始的时候都自定义 User 模型
- Resume 权限
    - 未登录用户无权限
    - `superuser` 可编辑所有
    - `HR` 组成员可以查看所有
    - `Interviewer` 组成员仅可以查看被分配给自己的候选人的简历
    - 其他一般登录用户仅查看、编辑和提交自己的简历
    - 自定义 action, `superuser` 和 `HR` 组成员可以将 `Resume` 转化为 `Candidate` 
- Candidate 权限
    - 未登录用户无权限
    - `superuser` 可编辑所有
    - `HR` 组成员可编辑所有
    - `Interviewer` 组成员仅可以查看被分配给自己的候选人信息
    - 其他一般登录用户无权限

## 缓存

- https://docs.djangoproject.com/en/4.0/topics/cache/
- Django 支持多种缓存实现 Memcached, Redis, 数据库, 文件, 内存和自定义方式的缓存
- Django 支持灵活的缓存策略, 包括:
    - 整站缓存
    - 视图缓存
    - 模版的部分内容缓存
    - 对 `Vary`, `Cache-Control` 等 header 字段配置