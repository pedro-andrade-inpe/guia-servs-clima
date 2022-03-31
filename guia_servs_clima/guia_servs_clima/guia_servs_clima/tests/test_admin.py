import pytest
from model_bakery import baker
from guia_servs_clima.guia_servs_clima.models import Organizacao
from guia_servs_clima.guia_servs_clima.admin import OrganizacaoAdmin
from django.contrib import admin


@pytest.fixture
def lista_organizacao_cadastro_aprovacao_false(db):
    """Cria uma lista do modelo Organizacao.

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma lista do modelo Organizacao.
    """
    org_list = baker.make(Organizacao, _quantity=20, cadastro_aprovacao=False)
    return org_list


@pytest.fixture
def lista_organizacao_cadastro_aprovacao_true(db):
    """Cria uma lista do modelo Organizacao.

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma lista do modelo Organizacao.
    """
    org_list = baker.make(Organizacao, _quantity=5, cadastro_aprovacao=True)
    return org_list


def test_make_published_true(lista_organizacao_cadastro_aprovacao_true):
    org_admin = OrganizacaoAdmin(Organizacao, admin.site)
    org_admin.make_published({}, Organizacao.objects.all())
    assert Organizacao.objects.filter(cadastro_aprovacao=True).count() == 5


def test_make_published_false(lista_organizacao_cadastro_aprovacao_false):
    assert Organizacao.objects.filter(cadastro_aprovacao=False).count() == 20
