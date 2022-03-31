from django import template

register = template.Library()


@register.simple_tag
def pagination_query_string(request, **kwargs):
    qs = request.GET.copy()
    qs.pop('page', None)
    return qs.urlencode()
