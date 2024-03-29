from django import template

register = template.Library()


@register.filter(name='next')
def next(object_list, current_index):
    """
    Returns the next element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        return object_list[int(current_index) + 1]  # access the next element
    except:
        return ''  # return empty string in case of exce


