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
