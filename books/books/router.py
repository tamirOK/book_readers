import random


class Router:
    def db_for_read(self, model, **hints):
        return random.choice(['master', 'slave'])

    def db_for_write(self, model, **hints):
        return 'master'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
