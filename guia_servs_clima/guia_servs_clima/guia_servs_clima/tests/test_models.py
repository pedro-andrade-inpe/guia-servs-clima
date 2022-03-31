import pytest
from model_bakery import baker

from django.conf import settings

from guia_servs_clima.guia_servs_clima.models import OrganizacaoTipoProduto


def test_organizacao_feito_upload_do_logo(organizacao_com_logo):
    """Testa se o caminho de uma logo de uma organizacao, se foi feito o upload.

    Args:
        organizacao_com_logo (fixture): Fixture que cria uma instância de Organização com logo.
    """
    assert organizacao_com_logo.organizacao_logo == '/media/org-logo.png'


def test_organizacao_sem_upload_logo_com_logo_default(organizacao_sem_logo):
    """Testa se está retornando o caminho default, quando não existe logo no momento da criação do organização.


    Args:
        organizacao_sem_logo (fixture): Fixture que cria uma instância de Organização sem logo.
    """
    assert organizacao_sem_logo.organizacao_logo == f"{settings.STATIC_URL}images/logo/default-logo.png"


def test_organizacao_tipo_produto_detalhes(organizacao_tipo_produto):
    """Testa o retorno do 'tipo de produto' e 'detalhes_servico' em organizacao_tipo_produto.


    Args:
        organizacao_tipo_produto (fixture): Cria uma instância do modelo OrganizacaoTipoProduto
         com o campo detalhes_servico preenchido.
    """
    assert organizacao_tipo_produto.organizacao.org_tipo_detalhes == {'Dados Brutos': 'Sou um Dado Bruto'}


@pytest.fixture
def organizacao_tipo_produto_sem_detalhes_servico_preenchido(organizacao_com_logo, tipos_produto):
    """Cria uma instância do modelo OrganizacaoTipoProduto com o campo detalhes_servico preenchido.

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma instância do modelo OrganizacaoTipoProduto.
    """
    organizacao_tipo_produto = baker.make(
        OrganizacaoTipoProduto,
        organizacao=organizacao_com_logo,
        tipo_produto=tipos_produto,
        detalhes_servico=""
    )
    return organizacao_tipo_produto


def test_organizacao_sem_o_campo_detalhes_servico_preenchido(
    organizacao_tipo_produto_sem_detalhes_servico_preenchido
):
    """Testa se no campo 'detalhes_servico' vem a string 'Sem detalhes cadastrados',
     quando o campo não é preenchido.


    Args:
        organizacao_tipo_produto_sem_detalhes_servico_preenchido (fixture):
        Cria uma instância do modelo OrganizacaoTipoProduto com o campo detalhes_servico não preenchido.
    """
    assert organizacao_tipo_produto_sem_detalhes_servico_preenchido.organizacao.org_tipo_detalhes == {
        'Dados Brutos': 'Sem detalhes cadastrados'}
