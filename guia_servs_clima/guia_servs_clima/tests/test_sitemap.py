import pytest
from django.urls import reverse

from guia_servs_clima.sitemap import OrganizacaoSitemap


@pytest.fixture
def resp_sitemap(db, client):
    """Fixture que da acesso a sitemap.xls

    Args:
        client (fixture): Uma instância de django.test.Client

    Returns:
        O acesso a página 'sitemap.xls'
    """
    resp = client.get(reverse('django.contrib.sitemaps.views.sitemap'))
    return resp


def test_sitemap_status_code(resp_sitemap):
    """Testa o acesso ao endpoint 'sitemap.xls', retonou sucesso (200)

    Args:
        resp_sitemap (fixture): Fixture que da acesso ao 'sitemap.xls'
    """
    resp_sitemap.status_code == 200


def test_sitemap_lista_organizacao(lista_organizacao):
    """Testa a lista de organização que está no sitemap

    Args:
        lista_organizacao (fixture): Cria uma lista do modelo Organizacao.
    """
    org_sitemap = OrganizacaoSitemap()
    org_sitemap.items().count() == len(lista_organizacao)


def test_sitemap_ordenacao(organizacao_com_logo, organizacao_sem_logo):
    """Testa a ordenação das ornizações dentro do sitemap

    """
    org_sitemap = OrganizacaoSitemap()
    org_sitemap.items().first() == organizacao_com_logo
