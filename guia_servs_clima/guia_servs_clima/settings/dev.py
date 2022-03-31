from .base import *


DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '150.163.2.227', "www.diiav.dpi.inpe.br", "www.diiav.dpi.inpe.br:8080", "diiav.dpi.inpe.br", "www.gclima.dpi.inpe.br", "www.gclima-forum.dpi.inpe.br"]

STATIC_ROOT =  os.path.join(BASE_DIR, 'assets/static/')
MEDIA_ROOT =  os.path.join(BASE_DIR, 'assets/media/')
