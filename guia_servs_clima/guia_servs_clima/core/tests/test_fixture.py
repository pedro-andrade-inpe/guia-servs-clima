from django.core import management


def test_carrega_guia_servicos_initial_fixtures(db):
    """
    Testa se a fixture 'guia_servicos_initial_fixtures' está sendo carregada com sucesso.
    """
    management.call_command('loaddata', 'guia_servicos_initial_fixtures.json', app_label='core', verbosity=0)
