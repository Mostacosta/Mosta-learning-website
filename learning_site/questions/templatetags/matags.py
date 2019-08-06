from django import template

register = template.Library()

@register.filter(name = "check")
def check(value,arg):
    if value in arg.all():
        return True
    else:
        return False
    