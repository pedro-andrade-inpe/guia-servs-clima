from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView

from .forms import OrganizacaoForm, OrgFilterForm
from .graficos import (grafico_barras_tipos_produtos,
                       grafico_pizza_tipos_organizacao)
from .models import Organizacao
from django.apps import apps


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = {
            'form': OrgFilterForm(queryset=None),
        }
        return context


class OrganizacaoCreateView(SuccessMessageMixin, CreateView):
    form_class = OrganizacaoForm
    model = Organizacao
    template_name = 'organizacao_form.html'
    success_message = 'Cadastro encaminhado para INPE para aprovação de divulgação.'
    success_url = reverse_lazy('home')


def filtrar_organizacao(request):
    template_name = 'filter.html'
    org_aprovacao = Organizacao.objects.filter(cadastro_aprovacao=True)
    search_form = OrgFilterForm(request.GET, queryset=org_aprovacao)

    if search_form.is_valid():
        org_aprovacao = search_form.get_queryset()

    page = Paginator(org_aprovacao, 6)

    if not org_aprovacao.count():
        messages.info(request, "Não existem provedores cadastrados que\
        atendam aos critérios selecionados. Por favor, refaça a busca.")
        context = {'messages': messages}

    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)
    context = {
        'org_aprovacao': org_aprovacao,
        'filter': search_form,
        'page_obj': page_obj
    }
    return render(request, template_name, context)


class OrganizacaoDetailView(DetailView):
    template_name = 'detalhes_organizacao.html'
    model = Organizacao

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        org_id = kwargs['object'].id
        setores_economicos = Organizacao.objects.setores_economicos(org_id)
        nome_setor = setores_economicos.values_list('nome', flat=True)
        ctx['setores_economicos'] = nome_setor
        ctx['cadastro_aprovacao'] = self.object.cadastro_aprovacao
        return ctx


class SaibaMaisView(TemplateView):
    template_name = 'saiba_mais.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        grafico_tipos_organizacao = grafico_pizza_tipos_organizacao()
        grafico_tipos_produtos = grafico_barras_tipos_produtos()
        ctx['figura_tipos_organizacao'] = grafico_tipos_organizacao
        ctx['figura_tipos_produtos'] = grafico_tipos_produtos
        return ctx


def municipio_ajax(request, uf, app_label, object_name):
    model_cls = apps.get_model(app_label, object_name)

    municipio_list = model_cls.objects.filter(uf=uf)
    return render(
        request,
        "municipios/municipios_options.html",
        {"municipio_list": municipio_list},
    )
