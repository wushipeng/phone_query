from django import template
from django.utils.html import format_html


register = template.Library()


@register.simple_tag
def limit_tr(cityinfo,cityobj):
    if (list(cityobj).index(cityinfo)+1) % 3 == 0:
        td_html ="<td>%s:%s</td></tr><tr>" % (cityinfo["city_name"],cityinfo["phone_number"])

    else:
        td_html = "<td>%s:%s</td>" % (cityinfo["city_name"],cityinfo["phone_number"])
    return format_html(td_html)


@register.simple_tag
def limit_page(current_page, pg):
    scope = abs(current_page - pg)

    if scope < 3:
        if current_page == pg:
            page_re = """<a class="current"> %s </a> """ % pg

        else:
            page_re = """<a href="?page=%s"> %s </a></li>""" % (pg, pg)
        return format_html(page_re)
    else:
        return ""