from guia_servs_clima.guia_servs_clima.forms import OrganizacaoForm
from guia_servs_clima.guia_servs_clima.forms import OrgFilterForm
from guia_servs_clima.guia_servs_clima.models import Organizacao


def test_organizacao_form_is_valid(
    municipios_municipio,
    tipos_produto,
    tipos_organizacao,
    tipos_pagamento,
    setores_economicos
):
    """Testa se o formulário Cadastro de Organização é válido.

    Args:
        municipios_municipio (fixture): Cria uma instância do modelo Municipio, \
            que herda da lib django-municipios.
        tipos_produto (fixture): Cria uma instância do modelo TipoProduto.
        tipos_organizacao (fixture): Cria uma instância do modelo TipoOrganizacao.
        tipos_pagamento (fixture): Cria uma instância do modelo TipoPagamento.
        setores_economicos (fixture): Cria uma instância do modelo SetorEconomico.
    """
    data = {
        'nome': 'Open Sea',
        'municipio': municipios_municipio.pk,
        'website_organizacao': 'www.opensea.com',
        'pessoa_contato': 'Open Sea Contato',
        'telefone_contato': '1234566773',
        'email_contato': 'opensea@email.com',
        'natureza_organizacao': 1,
        'logo': None,
        'sobre_organizacao': 'sdads',
        'tipos_organizacao': [tipos_organizacao.pk, ],
        'tipos_produto': [tipos_produto.pk, ],
        'tipos_pagamento': [tipos_pagamento.pk, ],
        'setores_economicos': [setores_economicos.pk, ],
        'observacao_adicional': 'sdsadsa',
        'politica_privacidade': True,
        'termo_uso': True
    }
    form = OrganizacaoForm(data=data)
    assert form.is_valid() is True


def test_organizacao_form_is_not_valid(
    municipios_municipio,
    tipos_produto,
    tipos_organizacao,
    tipos_pagamento,
    setores_economicos
):
    """Testa se o formulário Cadastro de Organização não é valido.

    Args:
        municipios_municipio (fixture): Cria uma instância do modelo Municipio, \
            que herda da lib django-municipios.
        tipos_produto (fixture): Cria uma instância do modelo TipoProduto.
        tipos_organizacao (fixture): Cria uma instância do modelo TipoOrganizacao.
        tipos_pagamento (fixture): Cria uma instância do modelo TipoPagamento.
        setores_economicos (fixture): Cria uma instância do modelo SetorEconomico.
    """
    data = {
        'nome': 'Open Sea',
        'municipio': municipios_municipio.pk,
        'website_organizacao': 'www.opensea.com',
        'pessoa_contato': 'Open Sea Contato',
        'telefone_contato': '1234566773',
        'email_contato': 'opensea@email.com',
        'natureza_organizacao': 1,
        'logo': None,
        'sobre_organizacao': 'sdads',
        'tipos_organizacao': [tipos_organizacao.pk, ],
        'tipos_produto': [tipos_produto.pk, ],
        'tipos_pagamento': [tipos_pagamento.pk, ],
        'setores_economicos': [setores_economicos.pk, ],
        'observacao_adicional': 'sdsadsa',
        'politica_privacidade': True,
        'termo_uso': False
    }
    form = OrganizacaoForm(data=data)
    assert form.is_valid() is False


def test_organizacao_se_o_campo_politica_privacidade_e_termo_uso_is_checked(
    municipios_municipio,
    tipos_produto,
    tipos_organizacao,
    tipos_pagamento,
    setores_economicos
):
    """Testa se o formulário apresenta o erro do campo politica_de_dados.

    Args:
        municipios_municipio (fixture): Cria uma instância do modelo Municipio, \
            que herda da lib django-municipios.
        tipos_produto (fixture): Cria uma instância do modelo TipoProduto.
        tipos_organizacao (fixture): Cria uma instância do modelo TipoOrganizacao.
        tipos_pagamento (fixture): Cria uma instância do modelo TipoPagamento.
        setores_economicos (fixture): Cria uma instância do modelo SetorEconomico.
    """
    data = {
        'nome': 'Open Sea',
        'municipio': municipios_municipio.pk,
        'website_organizacao': 'www.opensea.com',
        'pessoa_contato': 'Open Sea Contato',
        'telefone_contato': '1234566773',
        'email_contato': 'opensea@email.com',
        'natureza_organizacao': 1,
        'logo': None,
        'sobre_organizacao': 'sdads',
        'tipos_organizacao': [tipos_organizacao.pk, ],
        'tipos_produto': [tipos_produto.pk, ],
        'tipos_pagamento': [tipos_pagamento.pk, ],
        'setores_economicos': [setores_economicos.pk, ],
        'observacao_adicional': 'sdsadsa',
        'politica_privacidade': False,
        'termo_uso': False

    }
    form = OrganizacaoForm(data=data)
    assert form.errors == {
        'politica_privacidade': ['Por favor indicar que concorda com a Política de Privacidade.'],
        'termo_uso': ['Por favor indicar que concorda com o Termo de Uso.']
    }


def test_custom_checkbox_select_multiple_image(tipos_organizacao):
    """Testa o slug do campo 'tipos_organizacao' para gerar a imagem do chackbox.

    Args:
        tipos_organizacao (fixture): Cria uma instância do modelo TipoOrganizacao.
    """
    form = OrganizacaoForm()
    assert f'slug="{tipos_organizacao.slug}"' in str(form['tipos_organizacao'])


def test_form_campo_uf_selecionado_disponivel(
    municipios_municipio,
    tipos_produto,
    tipos_organizacao,
    tipos_pagamento,
    setores_economicos
):

    data = {
        'nome': 'Teste Cadastro 1',
        'municipio': municipios_municipio.pk,
        'website_organizacao': 'www.testecadastro.com',
        'pessoa_contato': 'Teste1',
        'telefone_contato': '1234566774',
        'email_contato': 'teste1@email.com',
        'uf_selecionado': 26,
        'natureza_organizacao': 1,
        'logo': None,
        'sobre_organizacao': 'sdads',
        'tipos_organizacao': [tipos_organizacao.pk, ],
        'tipos_produto': [tipos_produto.pk, ],
        'tipos_pagamento': [tipos_pagamento.pk, ],
        'setores_economicos': [setores_economicos.pk, ],
        'observacao_adicional': 'sdsadsa',
        'politica_privacidade': False,
        'termo_uso': False

    }

    form = OrganizacaoForm(data=data)
    assert form.data['uf_selecionado'] == 26


def test_form_campo_municipio_selecionado_disponivel(
    municipios_municipio,
    tipos_produto,
    tipos_organizacao,
    tipos_pagamento,
    setores_economicos
):

    data = {
        'nome': 'Teste Cadastro 2',
        'municipio': municipios_municipio.pk,
        'website_organizacao': 'www.testecadastro2.com',
        'pessoa_contato': 'Teste2',
        'telefone_contato': '1234566775',
        'email_contato': 'teste2@email.com',
        'uf_selecionado': 26,
        'municipio_selecionado': 'Recife',
        'natureza_organizacao': 1,
        'logo': None,
        'sobre_organizacao': 'sdads',
        'tipos_organizacao': [tipos_organizacao.pk, ],
        'tipos_produto': [tipos_produto.pk, ],
        'tipos_pagamento': [tipos_pagamento.pk, ],
        'setores_economicos': [setores_economicos.pk, ],
        'observacao_adicional': 'sdsadsa',
        'politica_privacidade': False,
        'termo_uso': False

    }

    form = OrganizacaoForm(data=data)
    assert form.data['municipio_selecionado'] == 'Recife'


def test_organizacao_form_is_valid_sem_campo_website_organizacao_como_obrigatorio(
    municipios_municipio,
    tipos_produto,
    tipos_organizacao,
    tipos_pagamento,
    setores_economicos
):
    """Testa se o formulário Cadastro de Organização é válido.

    Args:
        municipios_municipio (fixture): Cria uma instância do modelo Municipio, \
            que herda da lib django-municipios.
        tipos_produto (fixture): Cria uma instância do modelo TipoProduto.
        tipos_organizacao (fixture): Cria uma instância do modelo TipoOrganizacao.
        tipos_pagamento (fixture): Cria uma instância do modelo TipoPagamento.
        setores_economicos (fixture): Cria uma instância do modelo SetorEconomico.
    """
    data = {
        'nome': 'Open Sea',
        'municipio': municipios_municipio.pk,
        'website_organizacao': '',
        'pessoa_contato': 'Open Sea Contato',
        'telefone_contato': '1234566773',
        'email_contato': 'opensea@email.com',
        'natureza_organizacao': 1,
        'logo': None,
        'sobre_organizacao': 'sdads',
        'tipos_organizacao': [tipos_organizacao.pk, ],
        'tipos_produto': [tipos_produto.pk, ],
        'tipos_pagamento': [tipos_pagamento.pk, ],
        'setores_economicos': [setores_economicos.pk, ],
        'observacao_adicional': 'sdsadsa',
        'politica_privacidade': True,
        'termo_uso': True
    }
    form = OrganizacaoForm(data=data)
    assert form.is_valid() is True


def test_filtra_organizacao(
    tipos_produto,
    tipos_organizacao,
    tipos_pagamento,
    setores_economicos,
    organizacao_filtro_setores_econonicos,
    organizacao_filtro_tipos_organizacao,
    organizacao_filtro_tipos_produto,
    organizacao_filtro_tipos_pagamento
):
    """Testa se no filtro de organizacao na página home está pesquisando por no mínimo um item.

    Args:
        tipos_produto (fixture): Cria uma instância do modelo TipoProduto.
        tipos_organizacao (fixture): Cria uma instância do modelo TipoOrganizacao.
        tipos_pagamento (fixture): Cria uma instância do modelo TipoPagamento.
        setores_economicos (fixture): Cria uma instância do modelo SetorEconomico.
        organizacao_filtro_setores_econonicos (fixture): Cria uma instância do modelo Organizacao, \
            o campo cadastro_aprovacao=True, cadastro aprovado. E adicionando à organizacao um\
                 'setore_economico'
        organizacao_filtro_tipos_organizacao (fixture): Cria uma instância do modelo Organizacao,\
             o campo cadastro_aprovacao=True, cadastro aprovado. E adicionando à organizacao um\
                  'tipo de organizacao'
        organizacao_filtro_tipos_produto (fixture): Cria uma instância do modelo Organizacao, \
            o campo cadastro_aprovacao=True, cadastro aprovado. E adicionando à organizacao um \
                'tipo de produto'
        organizacao_filtro_tipos_pagamento (fixture): Cria uma instância do modelo Organizacao, \
            o campo cadastro_aprovacao=True, cadastro aprovado. E adicionando à organizacao um \
                'tipo de pagamento'

    """
    org_aprovacao = Organizacao.objects.filter(cadastro_aprovacao=True)
    data = {
        'tipos_organizacao': [tipos_organizacao.pk, ],
        'tipos_produto': [tipos_produto.pk, ],
        'tipos_pagamento': [tipos_pagamento.pk, ],
        'setores_economicos': [setores_economicos.pk, ],
    }
    form = OrgFilterForm(data=data, queryset=org_aprovacao)
    form.is_valid()
    assert form.get_queryset().filter(pk=organizacao_filtro_setores_econonicos.pk).exists()
    assert form.get_queryset().filter(pk=organizacao_filtro_tipos_organizacao.pk).exists()
    assert form.get_queryset().filter(pk=organizacao_filtro_tipos_produto.pk).exists()
    assert form.get_queryset().filter(pk=organizacao_filtro_tipos_pagamento.pk).exists()


def test_filtro_sem_organizacao(
    tipos_produto,
    tipos_organizacao,
    tipos_pagamento,
    setores_economicos

):
    """Testa se no filtro de organizacao na página home a pesquisa está vazia.

    Args:
        tipos_produto (fixture): Cria uma instância do modelo TipoProduto.
        tipos_organizacao (fixture): Cria uma instância do modelo TipoOrganizacao.
        tipos_pagamento (fixture): Cria uma instância do modelo TipoPagamento.
        setores_economicos (fixture): Cria uma instância do modelo SetorEconomico.
    """
    org_aprovacao = Organizacao.objects.filter(cadastro_aprovacao=True)
    data = {}
    form = OrgFilterForm(data=data, queryset=org_aprovacao)
    form.is_valid()
    assert form.get_queryset().count() == 0
