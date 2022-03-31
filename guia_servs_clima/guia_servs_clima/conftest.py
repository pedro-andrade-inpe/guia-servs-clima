import pytest
from django.urls import reverse
from model_bakery import baker

from guia_servs_clima.guia_servs_clima.models import (Organizacao,
                                                      OrganizacaoTipoProduto,
                                                      SetorEconomico,
                                                      TipoOrganizacao,
                                                      TipoPagamento,
                                                      TipoProduto)


@pytest.fixture
def resp_home(db, client):
    """Fixture que da acesso ao endpoint 'home'

    Args:
        client (fixture): Uma instância de django.test.Client

    Returns:
        Usuario com acesso a página 'home'
    """
    resp = client.get(reverse('home'))
    return resp


@pytest.fixture
def resp_cria_organizacao(db, client):
    """Fixture que da acesso ao endpoint 'organizacao_criar'

    Args:
        client (fixture): Uma instância de django.test.Client

    Returns:
        Usuario com acesso a página 'organizacao_criar'
    """
    resp = client.get(reverse('organizacao_criar'))
    return resp


@pytest.fixture
def resp_filtrar_organizacao(db, client):
    """Fixture que da acesso ao endpoint 'organizacao_filtro'

    Args:
        client (fixture): Uma instância de django.test.Client

    Returns:
        Usuario com acesso a página 'organizacao_filtro'
    """
    resp = client.get(reverse('organizacao_filtro'))
    return resp


@pytest.fixture
def resp_saiba_mais(db, client):
    """Fixture que da acesso ao endpoint 'saiba_mais'

    Args:
        client (fixture): Uma instância de django.test.Client

    Returns:
        O acesso a página 'saiba_mais'
    """
    resp = client.get(reverse('saiba_mais'))
    return resp


@pytest.fixture
def resp_lista_organizacao(db, client):
    resp = client.get(reverse('organizacao_filtro'))
    return resp


@pytest.fixture
def tipos_produto(db):
    """Cria uma instância do modelo TipoProduto.

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma instância do modelo TipoProduto.
    """
    tipo_produto = baker.make(TipoProduto, nome="Dados Brutos")
    return tipo_produto


@pytest.fixture
def tipos_produto_2(db):
    """Cria uma instância do modelo TipoProduto.

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma instância do modelo TipoProduto.
    """
    tipo_produto = baker.make(TipoProduto)
    return tipo_produto


@pytest.fixture
def tipos_organizacao(db):
    """Cria uma instância do modelo TipoOrganizacao.

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma instância do modelo TipoOrganizacao.
    """
    tipo_organizacao = baker.make(TipoOrganizacao)
    return tipo_organizacao


@pytest.fixture
def tipos_pagamento(db):
    """Cria uma instância do modelo TipoPagamento.

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma instância do modelo TipoPagamento.
    """
    tipo_pagamento = baker.make(TipoPagamento)
    return tipo_pagamento


@pytest.fixture
def setores_economicos(db):
    """Cria uma instância do modelo SetorEconomico.

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma instância do modelo SetorEconomico.
    """
    setor = baker.make(SetorEconomico)
    return setor


@pytest.fixture
def municipios_municipio(db):
    """Cria uma instância do modelo Municipio, que herda da lib django-municipios.

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma instância do modelo Municipio.
    """
    municipio = baker.make('municipios.Municipio')
    return municipio


@pytest.fixture
def organizacao_com_logo(setores_economicos):
    org_logo = baker.make(Organizacao, nome='OrgTesteLogo', logo='org-logo.png')
    org_logo.setores_economicos.add(setores_economicos.pk)
    return org_logo


@pytest.fixture
def organizacao_sem_logo(db):
    org_sem_logo = baker.make(Organizacao, nome='OrgTesteSemLogo')
    return org_sem_logo


@pytest.fixture
def organizacao_filtro_setores_econonicos(setores_economicos):
    """Cria uma instância do modelo Organizacao, o campo cadastro_aprovacao=True, cadastro aprovado.
    E adicionando à organizacao um 'setore_economico'

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma instância do modelo Organizacao.
    """
    org_filtro = baker.make(Organizacao, nome='OrgTesteSetor', cadastro_aprovacao=True)
    org_filtro.setores_economicos.add(setores_economicos.pk)
    return org_filtro


@pytest.fixture
def organizacao_filtro_tipos_organizacao(tipos_organizacao):
    """Cria uma instância do modelo Organizacao, o campo cadastro_aprovacao=True, cadastro aprovado.
    E adicionando à organizacao um 'tipo de organizacao'

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma instância do modelo Organizacao.
    """
    org_filtro = baker.make(Organizacao, nome='OrgTesteTipoOrg', cadastro_aprovacao=True)
    org_filtro.tipos_organizacao.add(tipos_organizacao.pk)
    return org_filtro


@pytest.fixture
def organizacao_filtro_tipos_produto(tipos_produto):
    """Cria uma instância do modelo Organizacao, o campo cadastro_aprovacao=True, cadastro aprovado.
    E adicionando à organizacao um 'tipo de produto'

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma instância do modelo Organizacao.
    """
    org_filtro = baker.make(Organizacao, nome='OrgTesteTiposProd', cadastro_aprovacao=True)
    org_filtro.tipos_produto.add(tipos_produto.pk)
    return org_filtro


@pytest.fixture
def organizacao_filtro_tipos_pagamento(tipos_pagamento):
    """Cria uma instância do modelo Organizacao, o campo cadastro_aprovacao=True, cadastro aprovado.
    E adicionando à organizacao um 'tipo de pagamento'

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma instância do modelo Organizacao.
    """
    org_filtro = baker.make(Organizacao, nome='OrgTesteTiposPag', cadastro_aprovacao=True)
    org_filtro.tipos_pagamento.add(tipos_pagamento.pk)
    return org_filtro


@pytest.fixture
def lista_organizacao(db):
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
    org_list = baker.make(Organizacao, _quantity=20)
    return org_list


@pytest.fixture
def organizacao_tipo_produto(organizacao_com_logo, tipos_produto):
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
        detalhes_servico="Sou um Dado Bruto"
    )
    return organizacao_tipo_produto


@pytest.fixture
def organizacao_tipo_produto_detalhes_servico_vazio(organizacao_com_logo, tipos_produto_2):
    """Cria uma instância do modelo OrganizacaoTipoProduto com o campo detalhes_servico vazio.

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
        tipo_produto=tipos_produto_2,
        detalhes_servico=""
    )
    return organizacao_tipo_produto
