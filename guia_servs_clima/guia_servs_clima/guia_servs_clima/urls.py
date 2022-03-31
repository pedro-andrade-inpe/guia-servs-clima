from django.urls import path

from guia_servs_clima.guia_servs_clima import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(
        "organizacao/criar/",
        views.OrganizacaoCreateView.as_view(),
        name="organizacao_criar",
    ),
    path(
        "organizacao/detalhes/<int:pk>/",
        views.OrganizacaoDetailView.as_view(),
        name="organizacao_detalhes",
    ),
    path("organizacao/filtro/", views.filtrar_organizacao, name="organizacao_filtro"),
    path("saibamais/", views.SaibaMaisView.as_view(), name="saiba_mais"),
]
