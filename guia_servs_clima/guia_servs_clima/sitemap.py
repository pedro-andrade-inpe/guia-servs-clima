from django.contrib.sitemaps import Sitemap

from .guia_servs_clima.models import Organizacao


class OrganizacaoSitemap(Sitemap):

    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Organizacao.objects.all().order_by('nome')
