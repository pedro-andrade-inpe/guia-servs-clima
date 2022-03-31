from django.urls.base import reverse

from guia_servs_clima.django_assertions import assert_contains

# -------------------- TESTES TEMPLATES RELACIONADOS A PÁGINA HOME (INÍCIO) -------------------- #


def test_navbar_texto_gov_br_disponivel(resp_home):
    """Testa se no navbar o texto 'GOV BR' está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """

    assert_contains(resp_home, 'GOV BR')


def test_navbar_link_home_disponivel(resp_home):
    """Testa se no navbar o link 'GOV BR' está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """
    assert_contains(resp_home, reverse('home'))


def test_navbar_texto_orgao_governo_disponivel(resp_home):
    """Testa se no navbar o texto 'ORGÃOS DO GOVERNO' está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """

    assert_contains(resp_home, 'ORGÃOS DO GOVERNO')


def test_navbar_link_orgao_governo_disponivel(resp_home):
    """Testa se no navbar o link 'ORGÃOS DO GOVERNO' está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """
    assert_contains(resp_home, 'https://www.gov.br/pt-br/orgaos-do-governo/')


def test_navbar_texto_participe_disponivel(resp_home):
    """Testa se no navbar o texto 'PARTICIPE' está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """

    assert_contains(resp_home, 'PARTICIPE')


def test_navbar_link_participe_disponivel(resp_home):
    """Testa se no navbar o link 'PARTICIPE' está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """
    assert_contains(resp_home, 'https://www.gov.br/pt-br/participacao-social/')


def test_navbar_texto_acesso_a_informacao_disponivel(resp_home):
    """Testa se no navbar o texto 'ACESSO À INFORMAÇÃO' está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """

    assert_contains(resp_home, 'ACESSO À INFORMAÇÃO')


def test_navbar_link_acesso_a_informacao_disponivel(resp_home):
    """Testa se no navbar o link 'ACESSO À INFORMAÇÃO' está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """
    assert_contains(resp_home, 'https://www.gov.br/acessoainformacao/pt-br/')


def test_navbar_texto_legislacao_disponivel(resp_home):
    """Testa se no navbar o texto 'LEGISLAÇÃO' está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """

    assert_contains(resp_home, 'LEGISLAÇÃO')


def test_navbar_link_legislacao_disponivel(resp_home):
    """Testa se no navbar o link 'LEGISLAÇÃO' está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """
    assert_contains(resp_home, 'http://www4.planalto.gov.br/legislacao/')


def test_descricao_disponivel(resp_home):
    """Testa se no navbar o texto 'Faça o teste e descubra o melhor
     provedor de serviços climáticos para seu projeto!' está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """
    assert_contains(
        resp_home, """<p>O <strong>Guia Serviços Climáticos</strong> reúne iniciativas e organizações brasileiras
         que fornecem dados, informações e produtos relacionados ao tempo e clima e tem o objetivo guiar pessoas,
        projetos e organizações a encontrarem esses serviços.</p>"""
    )


def test_tipo_servicao_disponivel(resp_home):
    """Testa se no navbar o texto 'Que tipo de serviço você está buscando?'
     está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """
    assert_contains(resp_home, 'Que <strong>tipo de serviço</strong> você está buscando?')


def test_tipo_setores_economicos_disponivel(resp_home):
    """Testa se no navbar o texto 'Quais são os setores econômicos de interesse para seu projeto?'
     está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """

    assert_contains(resp_home, 'Quais são os <strong>setores e temas de interesse</strong> para seu projeto?')


def test_tipo_organicao_disponivel(resp_home):
    """Testa se no navbar o texto 'Você busca algum tipo específico de organização?'
     está disponível na view 'home'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'home'
    """

    assert_contains(resp_home, 'Você busca algum <strong>tipo específico de organização</strong>?')


def test_navbar_link_criar_organizacao_disponivel(resp_home):
    """Testa se no navbar o link 'organizacao_criar' está disponível na view 'organizacao_criar'.

    Args:
        resp_home (fixture): Fixture que da acesso ao endpoint 'organizacao_criar'
    """
    assert_contains(resp_home, reverse('organizacao_criar'))

# ---------------------- TESTES TEMPLATES RELACIONADOS A PÁGINA HOME (FIM) ---------------------- #

# -------------------- TESTES TEMPLATES RELACIONADOS A PÁGINA CRIAR ORGANIZAÇÃO (INÍCIO) -------------------- #


def test_cria_organizacao_descricao_disponivel(resp_cria_organizacao):
    """Testa se no navbar o texto 'Cadastre sua Organização em nossa rede'
       está disponível na view 'organizacao_criar'.

    Args:
        resp_cria_organizacao (fixture): Fixture que da acesso ao endpoint 'organizacao_criar'
    """

    assert_contains(resp_cria_organizacao, 'Cadastre sua organização em nossa rede')


def test_texto_botao_submeter_cadastro_disponivel(resp_cria_organizacao):
    """Testa se o texto do botão 'Submeter Cadastro' está disponível na página 'organizacao_criar'

    Args:
        resp_cria_organizacao (fixture): Fixture que da acesso ao endpoint 'organizacao_criar'
    """

    assert_contains(resp_cria_organizacao, 'Submeter Cadastro')


# -------------------- TESTES TEMPLATES RELACIONADOS A PÁGINA CRIAR ORGANIZAÇÃO (FIM) -------------------- #

# -------------------- TESTES TEMPLATES RELACIONADOS A PÁGINA LISTAR ORGANIZAÇÃO (INÍCIO) -------------------- #


def test_lista_organizacao_resultados_do_teste_disponivel(resp_lista_organizacao):
    """Testa se o texto 'Resultados do teste' está disponível na página 'organizacao_filtro'.

    Args:
        resp_lista_organizacao (fixture): Fixture que da acesso ao endpoint 'organizacao_filtro'
    """

    assert_contains(resp_lista_organizacao, 'Resultados do teste')


def test_lista_organizacao_filtros_disponivel(resp_lista_organizacao):
    """Testa se o texto 'Filtros:' está disponível na página 'organizacao_filtro'

    Args:
        resp_lista_organizacao (fixture): Fixture que da acesso ao endpoint 'organizacao_filtro'
    """

    assert_contains(resp_lista_organizacao, 'Filtros:')


def test_lista_organizacao_refazer_o_teste_disponivel(resp_lista_organizacao):
    """Testa se o texto do botão 'Refazer o teste' está disponível na página 'organizacao_filtro'

    Args:
        resp_lista_organizacao (fixture): Fixture que da acesso ao endpoint 'organizacao_filtro'
    """

    assert_contains(resp_lista_organizacao, 'Refazer o teste')


def test_lista_organizacao_ver_todas_as_organizacaoes_disponivel(resp_lista_organizacao):
    """Testa se o texto do botão 'Ver todas as organizações' está disponível na página 'organizacao_filtro'

    Args:
        resp_lista_organizacao (fixture): Fixture que da acesso ao endpoint 'organizacao_filtro'
    """

    assert_contains(resp_lista_organizacao, 'Ver todas as organizações')

# -------------------- TESTES TEMPLATES RELACIONADOS A PÁGINA LISTAR ORGANIZAÇÃO (FIM) -------------------- #

# -------------------- TESTES TEMPLATES RELACIONADOS A PÁGINA SAIBA MAIS (INICIO) -------------------- #


def test_saiba_mais_mostrar_imagem_graficos(resp_saiba_mais):
    """Testa o acesso ao endpoint 'saiba_mais' apresenta graficos (pela class).

    Args:
        resp_saiba_mais (fixture): Fixture que da acesso ao endpoint
        'resp_saiba_mais'
    """

    assert_contains(resp_saiba_mais, 'main-svg')


def test_saiba_mais_mostrar_carrosel_video(resp_saiba_mais):
    """Testa o acesso ao endpoint 'saiba_mais' apresenta
       o elemento carrosel_video(pelo id).

    Args:
        resp_saiba_mais (fixture): Fixture que da acesso ao endpoint
        'resp_saiba_mais'
    """
    assert_contains(resp_saiba_mais, 'YouTube video player')


def test_saiba_mais_mostra_botao_baixar_relatório(resp_saiba_mais):
    """Testa o acesso ao endpoint 'saiba_mais' apresenta
       elemento do botão Baixe o relatório Serviços Climáticos no Brasil
       (pelo id).

    Args:
        resp_saiba_mais (fixture): Fixture que da acesso ao endpoint\
        'resp_saiba_mais'
    """

    assert_contains(resp_saiba_mais, 'download-relatório')


def test_saiba_mais_contains_string(resp_saiba_mais):
    """Testa se a view 'saiba_mais' contém a string 'Se você tiver dúvidas ou reclamações...'

    Args:
        resp_saiba_mais (fixture): Fixture que da acesso ao endpoint 'resp_saiba_mais'
    """

    assert_contains(
        resp_saiba_mais,
        'Se você tiver dúvidas ou reclamações sobre este website, '
        'entre em contato conosco pelo e-mail: contato@dpi.inpe.br'
        in resp_saiba_mais.content.decode('utf-8')
    )
    assert_contains(
        resp_saiba_mais,
        'O cadastro será analisado pelo corpo gestor do Guia Serviços Climáticos. '
        'Assim que possível, entraremos em contato pelo e-mail fornecido no formulário. '
        'Para atualizar, alterar ou remover o cadastro, '
        'entre em contato com o administrador do GuiaClima através do e-mail: contato@dpi.inpe.br'
        in resp_saiba_mais.content.decode('utf-8')
    )

# -------------------- TESTES TEMPLATES RELACIONADOS A PÁGINA PÁGINA SAIBA MAIS(FIM) -------------------- #
