from django import template

from ..models import get_related_documents

register = template.Library()


@register.filter(name='get_related_documents')
def related_documents(model):
    return get_related_documents(model)
