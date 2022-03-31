"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from guia_servs_clima.guia_servs_clima.views import municipio_ajax

from django.contrib.flatpages import views
from .sitemap import OrganizacaoSitemap

sitemaps = dict(sitemap=OrganizacaoSitemap)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'municipios_app/ajax/municipios/(?P<uf>\w\w)/(?P<app_label>\w+)/(?P<object_name>\w+)/$',
            municipio_ajax, name='municipio_ajax'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^municipios_app/', include('municipios.urls')),
    path('', include('guia_servs_clima.guia_servs_clima.urls')),
    path('link-forum/', RedirectView.as_view(url=settings.LINK_FORUM, permanent=False), name='link-forum'),
    re_path(r'^(?P<url>.*/)$', views.flatpage)
]

# urlpatterns += [
#     re_path(r'^media/(?P<path>.*)$', serve, {
#         'document_root': settings.MEDIA_ROOT,
#     }),
# ]
urlpatterns += [
    re_path(r'^{}/(?P<path>.*)$'.format(settings.MEDIA_URL.strip('/')), serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
