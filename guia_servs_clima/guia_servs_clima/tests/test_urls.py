from guia_servs_clima.urls import urlpatterns


def test_urls_len():
    """Testa quantidade de urls existentes dentro pasta 'guia_servs_clima'."""
    assert 6 <= len(urlpatterns)
