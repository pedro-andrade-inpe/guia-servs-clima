import plotly.graph_objects as go
from plotly.offline import plot

from .models import Organizacao

# GRÁFICOS


def grafico_pizza_tipos_organizacao():
    """Gera gráfico de pizza da porcentagem dos tipos de organização

    Args: None
    Returns: plot_grafico: desenho do gráfico completo.
    """
    queryset = Organizacao.objects.tipos_organizacao()
    labels = [qs['nome'] for qs in queryset]
    valores = [qs['qtd'] for qs in queryset]

    cores = [
        '#E73331',
        '#1C3666',
        '#1D5AA0',
        '#EE7555',
        '#FBD3C4',
        '#9DA6AA',
        '#9FC9DD',
        '#1D5AA0',
        '#F28D6E',
        '#05184A',
    ]

    grafico_pizza = go.Pie(
        labels=labels,
        values=valores,
        marker_colors=cores,
        texttemplate='%{label}: %{percent:%f}',
        textfont=dict(family='Muli, sans serif', size=14, color='#05184A'),
        hoverinfo='label+percent',
        hovertemplate='%{label}: %{percent:%f}',
    )
    data = [grafico_pizza]
    layout = go.Layout(
        showlegend=False,
        width=700,
        height=450,
        title={
            'text': 'Quem são as organizações participantes?',
            'y': 0.9,
            'x': 0.8,
        },
        titlefont=dict(size=24, family='Muli', color='#05184A'),
        uniformtext_minsize=14,
        uniformtext_mode='hide',
    )
    fig = go.Figure(data=data, layout=layout)
    fig.update_traces(textposition='outside')
    plot_grafico = plot(fig, auto_open=False, output_type='div')
    return plot_grafico


def grafico_barras_tipos_produtos():
    """Gera gráfico de pizza da porcentagem dos tipos de produtos

    Args: None

    Returns: plot_grafico: desenho do gráfico completo.
    """
    queryset = Organizacao.objects.tipos_produto()
    labels = [qs['nome'] for qs in queryset]
    valores = [qs['qtd'] for qs in queryset]

    cores = [
        '#E73331',
        '#1C3666',
        '#1D5AA0',
        '#EE7555',
        '#FBD3C4',
        '#9DA6AA',
        '#9FC9DD',
        '#1D5AA0',
        '#F28D6E',
        '#05184A',
    ]
    grafico_barras = go.Bar(
        x=valores,
        y=labels,
        orientation='h',
        marker_color=cores,
        textfont=dict(family='Muli, sans serif', size=14, color='#05184A'),
        textposition='inside',
        hovertemplate='%{y}: %{x}',
    )
    data = [grafico_barras]
    layout = go.Layout(
        showlegend=False,
        width=700,
        height=450,
        title={
            'text': 'Dados, produtos e serviços disponíveis',
            'y': 0.9,
            'x': 0.9,
        },
        titlefont=dict(size=24, family='Muli', color='#05184A'),
    )
    fig = go.Figure(data=data, layout=layout)
    plot_grafico = plot(fig, auto_open=False, output_type='div')
    return plot_grafico
