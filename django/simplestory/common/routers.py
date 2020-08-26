import os

class SsDatabase(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ['ssusers']:
            return os.environ.get('SSDB_NAME')
        # Returning None is no opinion, defer to other routers or default database
        return 'default'
    def db_for_write(self, model, **hints):
        if model._meta.app_label in ['ssusers']:
            return os.environ.get('SSDB_NAME')
         # Returning None is no opinion, defer to other routers or default database
        return 'default'