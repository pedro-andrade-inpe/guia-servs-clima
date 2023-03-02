from django import forms
from django.db.models import Q
from municipios.widgets import SelectMunicipioWidget
from municipios.models import UF

from guia_servs_clima.guia_servs_clima.models import (
    Organizacao,
    OrganizacaoTipoProduto,
    TipoOrganizacao,
    SetorEconomico,
    TipoProduto,
    TipoPagamento
)


class CustomCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    option_template_name = 'django/forms/widgets/input.html'


class CustomCheckboxSelectMultipleImage(forms.CheckboxSelectMultiple):
    option_template_name = 'custom_option_template_name.html'

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['slug'] = value.instance.slug
        return option


class OrganizacaoForm(forms.ModelForm):
    class Meta:
        model = Organizacao
        fields = [
            "nome",
            "municipio",
            "website_organizacao",
            "pessoa_contato",
            "telefone_contato",
            "email_contato",
            "natureza_organizacao",
            "logo",
            "sobre_organizacao",
            "tipos_organizacao",
            "tipos_produto",
            "tipos_pagamento",
            "setores_economicos",
            "observacao_adicional",
            "politica_privacidade",
            "termo_uso"
        ]

        widgets = {
            "tipos_organizacao": CustomCheckboxSelectMultipleImage,
            "setores_economicos": CustomCheckboxSelectMultipleImage,
            "tipos_produto": CustomCheckboxSelectMultiple,
            "tipos_pagamento": CustomCheckboxSelectMultiple,
            "municipio": SelectMunicipioWidget(
                attrs={"class": "form-select"},
                app_label="guia_servs_clima",
                object_name="MunicipioOrdenado",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["sobre_organizacao"].widget.attrs[
            "placeholder"
        ] = "Fale um pouco sobre sua organização."
        self.fields["observacao_adicional"].widget.attrs["placeholder"] = (
            "Deixe um comentário para a equipe do CClima."
        )
        self.fields["pessoa_contato"].widget.attrs["placeholder"] = (
            "Apenas para comunicação com o administrador do CClima"
        )

        self.forms_tipos_produto = []
        for field_tipo_produto in list(self["tipos_produto"]):
            org_tipo_produto_form = OrganizacaoTipoProdutoForm(
                tipo_produto=field_tipo_produto.data["value"].instance, data=self.data
            )
            self.forms_tipos_produto.append(
                (
                    field_tipo_produto,
                    org_tipo_produto_form,
                )
            )
        self.lista_ufs = UF.objects.all().order_by('nome')
        try:
            self.uf_selecionado = int(self.data['municipio_uf'])
        except (KeyError, ValueError):
            self.uf_selecionado = None

        try:
            self.municipio_selecionado = int(self.data['municipio'])
        except (KeyError, ValueError):
            self.municipio_selecionado = None

    def clean_termo_uso(self):
        data = self.cleaned_data["termo_uso"]
        if not data:
            raise forms.ValidationError(
                "Por favor indicar que concorda com o Termo de Uso.")
        return data

    def clean_politica_privacidade(self):
        data = self.cleaned_data["politica_privacidade"]
        if not data:
            raise forms.ValidationError(
                "Por favor indicar que concorda com a Política de Privacidade.")
        return data

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        for checkbox, forms_detalhes in self.forms_tipos_produto:
            if checkbox.data["value"].instance in self.cleaned_data["tipos_produto"]:
                forms_detalhes.save(organizacao=instance)
        return instance


class OrganizacaoTipoProdutoForm(forms.Form):

    detalhes_servico = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 4,
                "placeholder": "Adicione uma descrição mais detalhada sobre este serviço incluindo referências e links sempre que possível\
                    \n(limite de 500 caracteres)",
                "style": "background:#9FC9DD; display: none;",
            },
        ),
        required=False,
        max_length=500,
        help_text="Você precisa digitar uma descrição",
    )

    def __init__(self, *args, **kwargs):
        self.tipo_produto = kwargs.pop("tipo_produto")
        kwargs["prefix"] = f"tp_{self.tipo_produto.pk}"
        super().__init__(*args, **kwargs)

    def save(self, organizacao):
        instance = OrganizacaoTipoProduto.objects.get(
            organizacao=organizacao, tipo_produto=self.tipo_produto
        )
        if self.is_valid():
            instance.detalhes_servico = self.cleaned_data["detalhes_servico"]
            instance.save()


class OrgFilterForm(forms.Form):
    tipos_organizacao = forms.ModelMultipleChoiceField(queryset=TipoOrganizacao.objects.all(),
                                                       widget=CustomCheckboxSelectMultipleImage,
                                                       required=False)

    setores_economicos = forms.ModelMultipleChoiceField(queryset=SetorEconomico.objects.all(),
                                                        widget=CustomCheckboxSelectMultipleImage,
                                                        required=False)

    tipos_produto = forms.ModelMultipleChoiceField(queryset=TipoProduto.objects.all(),
                                                   widget=CustomCheckboxSelectMultiple,
                                                   required=False)

    tipos_pagamento = forms.ModelMultipleChoiceField(queryset=TipoPagamento.objects.all(),
                                                     widget=CustomCheckboxSelectMultiple,
                                                     required=False)

    def __init__(self, *args, **kwargs):
        self.queryset = kwargs.pop('queryset')
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        q = Q()
        if self.cleaned_data['tipos_organizacao']:
            q |= Q(tipos_organizacao__in=self.cleaned_data['tipos_organizacao'])

        if self.cleaned_data['setores_economicos']:

            q |= Q(setores_economicos__in=self.cleaned_data['setores_economicos'])

        if self.cleaned_data['tipos_produto']:

            q |= Q(tipos_produto__in=self.cleaned_data['tipos_produto'])

        if self.cleaned_data['tipos_pagamento']:

            q |= Q(tipos_pagamento__in=self.cleaned_data['tipos_pagamento'])

        return self.queryset.filter(q).distinct()
