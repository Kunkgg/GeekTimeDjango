# Django
## 开始项目 

```
django-admin startproject <procject_name> [.]

python manage.py startapp <app_name>

python manage.py makemigrations

python manage.py migrate

python manage.py runserver [--settings path.to.settings_module] [host_ip:port]
```

## 添加第一个数据模型 Job 

岗位信息对象：

-   职位类别
-   职位名称
-   工作地点
-   职位职责
-   职位要求
-   创建人
-   创建日期
-   修改日期

## 定制 Job Admin

1. `list_display` 定义在 admin 列表页面显示的属性列表
1. `exclude` 定义在 admin 编辑页面隐藏的属性列表

## 匿名用户浏览职位列表及职位详情页面

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

## Django 命令行工具，候选人数据批量导入

1. 批量导入 `csv` 格式候选人数据
2. fake_candidate 命令行工具

## Admin 筛选器、排序、搜索

1. ModelAdmin.list_filter
1. ModelAdmin.ordering
1. ModelAdmin.search_fields

## LDAP 登录

1. https://github.com/etianen/django-python3-ldap
1. 批量导入帐号 `./manage.py ldap_sync_users`
1. 为指定帐号设置超级用户权限 `./manage.py ldap_promote <username>`