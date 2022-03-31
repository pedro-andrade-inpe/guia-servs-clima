import pytest
from django.conf import settings
from django.urls.base import reverse
from model_bakery import baker

from guia_servs_clima.django_assertions import assert_contains
from guia_servs_clima.guia_servs_clima.models import Organizacao, TipoPagamento


@pytest.fixture
def organizacao(db):
    org_logo = baker.make(Organizacao, nome='OrgTesteLogo')
    return org_logo


@pytest.fixture
def resp_home_org(organizacao, client):
    """Fixture que da acesso ao endpoint 'home'

    Args:
        client (fixture): Uma instância de django.test.Client

    Returns:
        Usuario com acesso a página 'home'
    """
    resp = client.get(reverse('home'))
    return resp


def test_home_status_code(resp_home_org):
    """Testa o acesso ao endpoint 'home', retonou sucesso (200)

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """

    assert resp_home_org.status_code == 200


def test_cria_organizacao_status_code(resp_cria_organizacao):
    """Testa o acesso ao endpoint 'organizacao_criar', retonou sucesso (200)

    Args:
        resp_cria_organizacao (fixture): Fixture que da acesso ao endpoint 'organizacao_criar'
    """

    assert resp_cria_organizacao.status_code == 200


def test_saiba_mais_status_code(resp_saiba_mais):
    """Testa o acesso ao endpoint 'saiba_mais', retonou sucesso (200)

    Args:
        resp_saiba_mais (fixture): Fixture que da acesso ao endpoint 'resp_saiba_mais'
    """

    assert resp_saiba_mais.status_code == 200


@pytest.fixture
def municipio(db):
    """Cria uma instância do modelo Municipio.

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido apenas para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        org: Retorna uma instância do modelo Municipio.
    """
    return baker.make('municipios.Municipio')


@pytest.fixture
def organizacao_criar_post(municipio, tipos_produto, tipos_pagamento, tipos_organizacao, setores_economicos, client):
    """Fixture que da acesso ao endpoint 'organizacao_criar'

    Args:
        client (fixture): Uma instância de django.test.Client

    Returns:
        Usuario com acesso a página 'organizacao_criar'
    """
    resp = client.post(reverse('organizacao_criar'), data={
        'nome': 'Teste',
        'municipio': municipio.pk,
        'website_organizacao': 'www.teste',
        'pessoa_contato': 'Eu',
        'telefone_contato': '21 997456789',
        'email_contato': 'teste@email.com',
        'natureza_organizacao': Organizacao.NATUREZAORGANIZACAO.ORGANIZACAOPUBLICA,
        'tipos_organizacao': [tipos_organizacao.pk],
        'tipos_produto': [tipos_produto.pk],
        'tipos_pagamento': [tipos_pagamento.pk],
        'setores_economicos': [setores_economicos.pk],
        'politica_privacidade': True,
        'termo_uso': True

    })
    return resp


def test_organizao_criar_submit_redirect(organizacao_criar_post):
    """Testa se ao preencher os dados para criar uma Organização,
       quando clicado no botão submit, o status_code retorna (302 Found),
       redirecionado para página de detalhes.

    Args:
        organizacao_criar_post (fixture): Fixture que da acesso ao endpoint 'organizacao_criar'
    """
    assert organizacao_criar_post.status_code == 302


def test_filtro_status_code(resp_filtrar_organizacao):
    """Testa o acesso ao endpoint 'organizacao_filtro', retonou sucesso (200)

    Args:
        resp_filtrar_organizacao (fixture): Fixture que da acesso ao endpoint 'organizacao_filtro'
    """
    assert resp_filtrar_organizacao.status_code == 200


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
    tipo_pagamento = baker.make(TipoPagamento, nome='Pago')
    return tipo_pagamento


@pytest.fixture
def resp_filtrar_organizacao_nehum_criterio_atendido(tipos_pagamento, client):
    """Fixture que da acesso ao endpoint 'organizacao_filtro' com um tipo de pagamento que não existe.

    Args:
        client (fixture): Uma instância de django.test.Client

    Returns:
        Usuario com acesso a página 'organizacao_filtro'
    """
    resp = client.get(reverse('organizacao_filtro'), {'tipos_pagamento': [tipos_pagamento.pk + 1]})
    return resp


def test_filtro_home_nehum_criterio_atendido(resp_filtrar_organizacao_nehum_criterio_atendido):
    """Testa a filtragem de uma organização onde o critério de pesquisa não foi atendido.
    Retornando a mensagem:  'Não existem provedores cadastrados que\
        atendam aos critérios selecionados. Por favor, refaça a busca.'

    Args:
        resp_filtrar_organizacao_nehum_criterio_atendido ([type]): [description]
    """
    assert_contains(resp_filtrar_organizacao_nehum_criterio_atendido, 'Não existem provedores cadastrados que\
        atendam aos critérios selecionados. Por favor, refaça a busca.')


@pytest.fixture
def organizacao_cadastro_aprovado(db):
    """Cria uma instância do modelo Organizacao, o campo cadastro_aprovacao=True, cadastro aprovado.

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma instância do modelo Organizacao.
    """
    org_aprovada = baker.make(Organizacao, nome='OrgTesteAprovado', cadastro_aprovacao=True)
    return org_aprovada


@pytest.fixture
def organizacao_cadastro_não_aprovado(db):
    """Cria uma instância do modelo Organizacao, o campo cadastro_aprovacao=False, cadastro não aprovado.

    Args:
    db: Esta fixture irá garantir que o banco de dados Django seja\
    configurado. Requerido para fixtures que desejam usar o\
    banco de dados.
    Referencia:
    https://pytest-django.readthedocs.io/en/latest/helpers.html#db

    Returns:
        Retorna uma instância do modelo Organizacao.
    """
    org_nao_aprovada = baker.make(Organizacao, nome='OrgTesteNaoAprovado', cadastro_aprovacao=False)
    return org_nao_aprovada


def test_filtra_organizacao_cadastro_nao_aprovado(
    resp_filtrar_organizacao, organizacao_cadastro_não_aprovado
):
    """Testa se ao cadastrar uma organização, o cadastro não foi aprovado, com isso a empresa não aparece na\
         lista de organizações.

    Args:
        resp_filtrar_organizacao (fixture): Fixture que da acesso ao endpoint 'organizacao_filtro'.
        organizacao_cadastro_aprovado (fixture): Cria uma instância do modelo Organizacao, o campo\
             cadastro_aprovacao=False, cadastro não aprovado.
    """
    assert resp_filtrar_organizacao.context['org_aprovacao'].exists() is False


def test_ate_seis_organizacoes_por_pagina(resp_filtrar_organizacao, organizacao_cadastro_aprovado):
    """ Testa verifica_apresenta_apenas_ate_seis_organizacoes_por_pagina.

    Args:
        resp_filtrar_organizacao (fixture): Fixture que da acesso ao endpoint 'organizacao_filtro'.
        organizacao_cadastro_aprovado (fixture): Cria uma instância do modelo Organizacao, o campo\
             cadastro_aprovacao=True, cadastro aprovado.
    """

    assert len(resp_filtrar_organizacao.context['page_obj'].object_list) <= 6


def test_path_relatorio_saiba_mais(resp_saiba_mais):
    """Testa se no response contém o caminho para o relatório 'Relatorio_Base_CSI_20191213.pdf'

    Args:
        resp_saiba_mais (fixture): Fixture que da acesso ao endpoint 'resp_saiba_mais'
    """
    arquivo_path = f"{settings.STATIC_URL}relatorio/Relatorio_Base_CSI_20191213.pdf"
    assert_contains(resp_saiba_mais, arquivo_path)


@pytest.fixture
def resp_detalhes_da_organizacao(
        organizacao_com_logo,
        organizacao_tipo_produto,
        organizacao_tipo_produto_detalhes_servico_vazio,
        client
):
    """Fixture que da acesso ao endpoint 'organizacao_detalhes'

    Args:
        client (fixture): Uma instância de django.test.Client

    Returns:
        Usuario com acesso a página 'organizacao_detalhes'
    """
    resp = client.get(reverse('organizacao_detalhes', kwargs={'pk': organizacao_com_logo.pk}))
    return resp


def test_detalhes_organizacao_status_code(resp_detalhes_da_organizacao):
    """Testa o acesso ao endpoint 'organizacao_detalhes', retonou sucesso (200)

    Args:
        resp_detalhes_da_organizacao (fixture): Fixture que da acesso ao endpoint 'organizacao_detalhes'
    """
    assert resp_detalhes_da_organizacao.status_code == 200


def test_detalhes_organizacao_setores_economicoss(resp_detalhes_da_organizacao, setores_economicos):
    """Testa o conteúdo do campo 'setores_aconomicos' dentro da view 'organizacao_detalhes'

    Args:
        resp_detalhes_da_organizacao (fixture): Fixture que da acesso ao endpoint 'organizacao_detalhes'
    """
    assert resp_detalhes_da_organizacao.context['setores_economicos'].first() == str(setores_economicos)
