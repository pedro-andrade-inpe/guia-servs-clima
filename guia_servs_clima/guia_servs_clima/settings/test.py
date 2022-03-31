from .base import *

# PARA RODAR SEM MIGRAÇÕES DESCOMENTE da linha 5 a 13

# class DisableMigrations(object):
#     def __contains__(self, item):
#         return True

#     def __getitem__(self, item):
#         return None


# MIGRATION_MODULES = DisableMigrations()

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']
