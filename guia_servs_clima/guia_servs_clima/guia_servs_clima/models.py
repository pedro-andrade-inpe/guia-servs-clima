from django.conf import settings
from django.db import models
from django.db.models import Count
from django.urls import reverse
from django.utils.text import slugify
from municipios.models import Municipio


class TipoOrganizacao(models.Model):

    nome = models.CharField("Nome do Tipo da Organização", max_length=100)

    class Meta:
        verbose_name = "Tipo de Organização"
        verbose_name_plural = "Tipos de Organização"
        ordering = ["pk"]

    def __str__(self):
        return self.nome

    @property
    def slug(self):
        return slugify(self.nome)


class SetorEconomico(models.Model):

    nome = models.CharField("Nome do Setor Economico", max_length=100)

    class Meta:
        verbose_name = "Setor Econômico"
        verbose_name_plural = "Setores Econômicos"
        ordering = ["pk"]

    def __str__(self):
        return self.nome

    @property
    def slug(self):
        return slugify(self.nome)


class TipoProduto(models.Model):

    nome = models.CharField("Nome do Tipo do Produto", max_length=100)

    class Meta:
        verbose_name = "Tipo do Produto"
        verbose_name_plural = "Tipos dos Produtos"

    def __str__(self):
        return self.nome


class TipoPagamento(models.Model):

    nome = models.CharField("Nome do Tipo de Pagamento", max_length=100)

    class Meta:
        verbose_name = "Tipo Pagamento"
        verbose_name_plural = "Tipos Pagamentos"

    def __str__(self):
        return self.nome


class OrganizacaoQuerySet(models.QuerySet):
    def tipos_organizacao(self):
        return TipoOrganizacao.objects.annotate(qtd=Count("organizacao")).values(
            "nome", "qtd"
        )

    def tipos_produto(self):
        return TipoProduto.objects.annotate(qtd=Count("organizacao")).values(
            "nome", "qtd"
        )

    def setores_economicos(self, org_id):
        return SetorEconomico.objects.filter(organizacao=org_id)


class OrganizacaoManager(models.Manager):
    def get_queryset(self):
        return OrganizacaoQuerySet(self.model, using=self._db)

    def tipos_organizacao(self):
        return self.get_queryset().tipos_organizacao()

    def tipos_produto(self):
        return self.get_queryset().tipos_produto()

    def setores_economicos(self, org_id):
        return self.get_queryset().setores_economicos(org_id)


class Organizacao(models.Model):
    class NATUREZAORGANIZACAO:
        ORGANIZACAOPUBLICA = 1
        ORGANIZACAOPRIVADA = 2
        ORGANIZACAOPUBLICOPRIVADA = 3
        ORGANIZACAONAOGOVERNAMENTAL = 4
        PESSOAFISICA = 5
        CHOICES = [
            (1, "Pública"),
            (2, "Privada"),
            (3, "Público-Privada"),
            (4, "Não Governamental"),
            (5, "Profissional Autônomo"),
        ]

    cadastro_aprovacao = models.BooleanField(
        verbose_name="Autorizar Cadastro/Atualização", default=False, null=True
    )
    nome = models.CharField(
        "Nome da Organização", max_length=100, null=False, blank=False, unique=True
    )
    municipio = models.ForeignKey(
        "municipios.Municipio",
        verbose_name="Município",
        on_delete=models.PROTECT,
        related_name="municipios",
        null=False,
        blank=False,
    )
    website_organizacao = models.URLField(
        "Site da Organização", max_length=100, blank=True
    )
    pessoa_contato = models.CharField(
        "Pessoa de contato para a rede Adapta Brasil MCTI",
        max_length=100,
        null=False,
        blank=False,
    )
    telefone_contato = models.CharField(
        "Telefone da Organização", max_length=14, null=False, blank=False
    )
    email_contato = models.EmailField(
        "Email da Organização", max_length=254, null=False, blank=False
    )
    natureza_organizacao = models.SmallIntegerField(
        "Natureza da Organização",
        choices=NATUREZAORGANIZACAO.CHOICES,
        null=False,
        blank=False,
    )
    logo = models.ImageField("Logo", blank=True, upload_to="organizacao_logos")

    sobre_organizacao = models.TextField("Sobre a Organização",
                                         max_length=1000, blank=True)
    tipos_organizacao = models.ManyToManyField(TipoOrganizacao,
                                               through='OrganizacaoTipoOrganizacao',
                                               through_fields=('organizacao', 'tipo_organizacao'),
                                               blank=False)
    setores_economicos = models.ManyToManyField(SetorEconomico,
                                                through='OrganizacaoSetorEconomico',
                                                through_fields=('organizacao', 'setor_economico'),
                                                blank=False)
    tipos_produto = models.ManyToManyField(TipoProduto,
                                           through='OrganizacaoTipoProduto',
                                           through_fields=('organizacao', 'tipo_produto'),
                                           blank=False)

    tipos_pagamento = models.ManyToManyField(TipoPagamento,
                                             through='OrganizacaoTipoPagamento',
                                             through_fields=('organizacao', 'tipo_pagamento'),
                                             blank=False)

    observacao_adicional = models.TextField("Informações Adicionais",
                                            max_length=1000, blank=True)

    politica_privacidade = models.BooleanField(
        verbose_name="Política de Privacidade", default=False, blank=True)

    termo_uso = models.BooleanField(
        verbose_name="Termo de Uso", default=False, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    objects = OrganizacaoManager()

    class Meta:
        verbose_name = "Organização"
        verbose_name_plural = "Organizações"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("organizacao_detalhes", args=[str(self.id)])

    @property
    def organizacao_logo(self):
        """Verifica se existe uma imagem(logo) na Organizacao,
        senão não foi informado imagem na criação da Organizacao.
        """
        if self.logo:
            return self.logo.url
        else:
            return f"{settings.STATIC_URL}images/logo/default-logo.png"

    @property
    def org_tipo_detalhes(self):
        """Verifica se no cadastro de uma organização, o campo 'detalhes_servico' foi preenchido,
        senão deve retornar a string 'Sem detalhes cadastrados'.
        """
        dict_org_tipo = {}
        for org_tipo in self.organizacaotipoproduto_set.filter(organizacao__pk=self.pk):
            if org_tipo.detalhes_servico:
                dict_org_tipo[org_tipo.tipo_produto.nome] = org_tipo.detalhes_servico
            else:
                dict_org_tipo[org_tipo.tipo_produto.nome] = "Sem detalhes cadastrados"
        return dict_org_tipo


class OrganizacaoTipoProduto(models.Model):
    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE)
    tipo_produto = models.ForeignKey(TipoProduto, verbose_name='Tipo Produto', on_delete=models.CASCADE)
    detalhes_servico = models.TextField("Detalhes dos Serviços", null=False)

    class Meta:
        unique_together = ["tipo_produto", "organizacao"]
        verbose_name = 'Tipo Produto'
        verbose_name_plural = 'Tipos Produtos'

    def __str__(self):
        return str(self.tipo_produto)


class OrganizacaoSetorEconomico(models.Model):
    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE)
    setor_economico = models.ForeignKey(SetorEconomico, verbose_name='Setor Econômico', on_delete=models.CASCADE)

    class Meta:
        unique_together = ["setor_economico", "organizacao"]
        verbose_name = 'Setor Econômico'
        verbose_name_plural = 'Setores Econômicos'

    def __str__(self):
        return str(self.setor_economico)


class OrganizacaoTipoOrganizacao(models.Model):
    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE)
    tipo_organizacao = models.ForeignKey(TipoOrganizacao, verbose_name='Tipo Organização', on_delete=models.CASCADE)

    class Meta:
        unique_together = ["tipo_organizacao", "organizacao"]
        verbose_name = 'Tipo Organização'
        verbose_name_plural = 'Tipos Organizações'

    def __str__(self):
        return str(self.tipo_organizacao)


class OrganizacaoTipoPagamento(models.Model):

    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE)
    tipo_pagamento = models.ForeignKey(TipoPagamento, verbose_name='Tipo Pagamento', on_delete=models.CASCADE)

    class Meta:
        unique_together = ["tipo_pagamento", "organizacao"]
        verbose_name = 'Tipo Pagamento'
        verbose_name_plural = 'Tipos Pagamentos'

    def __str__(self):
        return str(self.tipo_pagamento)


class MunicipioOrdenadoManager(models.Manager):
    def get_queryset(self):
        resultado_q = (
            super()
            .get_queryset()
            .extra(select={"nome_unaccent": "unaccent(nome)"})
            .order_by("nome_unaccent")
        )
        return resultado_q


class MunicipioOrdenado(Municipio):

    objects = MunicipioOrdenadoManager()

    class Meta:
        proxy = True
