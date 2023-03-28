from django import template
from worklink import settings, utils
from django.forms import CheckboxInput

register = template.Library()


def media_folder_products(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам продуктов
    products_images/product1.jpg --> /media/products_images/product1.jpg
    """
    if not string:
        string = 'products_images/default.jpg'

    return f'{settings.MEDIA_URL}{string}'


@register.filter(name='media_folder_users')
def media_folder_users(string):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам пользователей
    users/user1.jpg --> /media/users/user1.jpg
    """
    if not string:
        string = 'avatar.png'

    return f'{settings.MEDIA_URL}{string}'


@register.filter(name='is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__


@register.filter(is_safe=True)
def label_with_classes(value, arg):
    return value.label_tag(attrs={'class': arg})


register.filter('media_folder_products', media_folder_products)

register.filter('price_format', utils.get_price_format)


@register.filter
def keyvalue(d, key):
    """
    Дает возможность использовать выражение типа {{dictionary|keyvalue:key_variable}} в шаблонах
    """
    return d[key]
