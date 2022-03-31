import pytest
from model_bakery import baker

from ..graficos import (grafico_barras_tipos_produtos,
                        grafico_pizza_tipos_organizacao)
from ..models import Organizacao, TipoOrganizacao, TipoProduto


@pytest.fixture
def tipo_organizacao(db):
    tipo_organizacao = baker.make(TipoOrganizacao)
    return tipo_organizacao


@pytest.fixture
def tipo_produto(db):
    tipo_produto = baker.make(TipoProduto)
    return tipo_produto


@pytest.fixture
def organizacao(db):
    organizacao = baker.make(Organizacao)
    return organizacao


def test_grafico_pizza_tipos_organizacao(organizacao, tipo_organizacao):
    plot = grafico_pizza_tipos_organizacao()
    assert plot != ''


def test_grafico_barras_tipos_produtos(organizacao, tipo_produto):
    plot = grafico_barras_tipos_produtos()
    assert plot != ''
