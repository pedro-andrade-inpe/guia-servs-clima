from django.contrib import admin

from guia_servs_clima.guia_servs_clima.models import (
    Organizacao,
    SetorEconomico,
    TipoOrganizacao,
    TipoPagamento,
    TipoProduto
)


class TipoOrganizacaoInlineAdmin(admin.TabularInline):
    model = Organizacao.tipos_organizacao.through


class SetorEconomicoInlineAdmin(admin.TabularInline):
    model = Organizacao.setores_economicos.through


class TipoProdutoInlineAdmin(admin.TabularInline):
    model = Organizacao.tipos_produto.through


class TipoPagamentoInlineAdmin(admin.TabularInline):
    model = Organizacao.tipos_pagamento.through


class OrganizacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'natureza_organizacao', 'cadastro_aprovacao', 'criado_em', 'atualizado_em')
    search_fields = ['nome']
    list_filter = ('cadastro_aprovacao',)
    actions = ['make_published']
    inlines = (TipoOrganizacaoInlineAdmin, SetorEconomicoInlineAdmin,
               TipoProdutoInlineAdmin, TipoPagamentoInlineAdmin,)

    def make_published(OrganizacaoAdmin, request, queryset):
        queryset.update(cadastro_aprovacao=True)
    make_published.short_description = 'Aprovar cadastro das organizações selecionadas'


class TipoOrganizacaoAdmin(admin.ModelAdmin):
    search_fields = ['nome']


class TipoProdutoAdmin(admin.ModelAdmin):
    search_fields = ['nome']


class TipoPagamentoAdmin(admin.ModelAdmin):
    search_fields = ['nome']


class SetorEconomicoAdmin(admin.ModelAdmin):
    search_fields = ['nome']


admin.site.register(Organizacao, OrganizacaoAdmin)
admin.site.register(TipoOrganizacao, TipoOrganizacaoAdmin)
admin.site.register(TipoProduto, TipoProdutoAdmin)
admin.site.register(TipoPagamento, TipoPagamentoAdmin)
admin.site.register(SetorEconomico, SetorEconomicoAdmin)
