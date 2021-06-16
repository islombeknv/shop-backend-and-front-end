from django import template
from django.db.models import Sum

from pages.utils import get_cart_length
from products.models import ProductModel

register = template.Library()


@register.simple_tag
def get_lang_url(request, lang):
    url = request.path.split('/')
    url[1] = lang
    return '/'.join(url)
    # return '/' + lang + request.path[3:]


@register.simple_tag
def get_price(request, x):
    price = request.GET.get('price')
    if price:
        return price.split(';')[x]
    return 'null'


@register.filter
def in_wishlist(product, request):
    return request.user in product.wishlist.all()


@register.filter
def in_cart(product, request):
    return product.pk in request.session.get('cart', [])


@register.simple_tag
def cart_count(request):
    return get_cart_length(request)
    # cart = request.session.get('cart', [])
    # return len(cart)


@register.simple_tag
def cart_price(request):
    if get_cart_length(request) == 0:
        return 0

    return ProductModel.get_from_cart(request).aggregate(
        Sum('real_price')
    )['real_price__sum']