from django import template
from pages.models import Categories
from googletrans import Translator

register = template.Library()


def translator_text(text):
    connect_trans = Translator()
    return connect_trans.translate(text, dest='ru').text


@register.simple_tag()
def get_categories():
    return Categories.objects.all()


@register.simple_tag()
def get_path_page(path):
    list_text_in_path = list(filter(lambda t: len(t) > 0, str(path).split('/')))
    if '-' in list_text_in_path[::-1][0]:
        trash_obj = list_text_in_path[::-1][0]
        list_text_in_path.remove(trash_obj)

    content = list(map(translator_text, list_text_in_path))
    content.insert(0, 'Главна страница')

    return [word.capitalize for word in content]

