class PostgreSQLDBRouter:
    """
    A router to control all database operations on models in the
    hello and contenttypes applications.
    """
    # route_app_labels = {'hello', 'contenttypes'}
    route_app_labels = {'hello'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read hello and contenttypes models go to postgresql.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'postgresql'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write hello and contenttypes models go to postgresql.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'postgresql'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the hello or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the hello and contenttypes apps only appear in the
        'postgresql' database.
        """
        if app_label in self.route_app_labels:
            return db == 'postgresql'
        return None