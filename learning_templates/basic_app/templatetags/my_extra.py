from django import template

register = template.library()
@register.filter(name='cut_function')
def cut_function(value,arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg,'')

# register.filter('cut',cut_function)
