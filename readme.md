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
1. namespace
1. include
1. reverse
    -   需要映射有 `name`
    -   在模版中使用 `url` 标签
    -   在 Python 代码中使用 `reverse` 函数

