# settings/router.py
# database router to multiple database by app label
class DatabaseRouter:
    route_app_labels = {'toy'}

    def db_for_read(self, model, **hints):
        rv = 'default'
        if model._meta.app_label in self.route_app_labels:
            rv = 'toy'
        return rv

    def db_for_write(self, model, **hints):
        rv = 'default'
        if model._meta.app_label in self.route_app_labels:
            rv = 'toy'
        return rv

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        遗留数据库中的表不允许迁移
        """
        return app_label not in self.route_app_labels
