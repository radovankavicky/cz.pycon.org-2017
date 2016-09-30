from django import template

from pyconcz_2016.sponsors.models import Sponsor

register = template.Library()


@register.inclusion_tag('sponsors/list.html')
def sponsors():
    items = Sponsor.objects.all().filter(published=True)
    return {'sponsors': items}
