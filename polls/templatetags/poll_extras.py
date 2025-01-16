from django import template
register = template.Library()
from jalali_date import date2jalali, datetime2jalali


@register.filter(name='j_time')
def j_time(value):
    res = datetime2jalali(value)
    return res

