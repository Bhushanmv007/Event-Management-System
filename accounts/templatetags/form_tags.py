from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    print("Custom tag 'add_class' loaded!")  # Debug statement
    return value.as_widget(attrs={'class': arg})
