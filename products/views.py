from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Min, Max
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from products.models import ProductModel, ProductTagModel, BrandModel, CategoryModel, SizeModel, ColorModel


class ProductlistView(ListView):
    template_name = 'shop.html'
    paginate_by = 3

    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')
        sort = self.request.GET.get('sort')
        size = self.request.GET.get('size')
        color = self.request.GET.get('color')
        price = self.request.GET.get('price')
        if q:
            qs = qs.filter(title__icontains=q)

        if cat:
            qs = qs.filter(category_id=cat)

        if brand:
            qs = qs.filter(brand_id=brand)

        if tag:
            qs = qs.filter(tags__id=tag)

        if sort:
            if sort == 'price':
                qs = sorted(qs, key=lambda i: i.get_price())
            elif sort == '-price':
                qs = sorted(qs, key=lambda i: i.get_price(), reverse=True)
        if size:
            qs = qs.filter(sizes__id=size)

        if color:
            qs = qs.filter(colors__id=color)

        if price:
            price = price.split(';')
            price_from, price_to = price
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = ProductTagModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['categories'] = CategoryModel.objects.all()
        context['sizes'] = SizeModel.objects.all()
        context['colors'] = ColorModel.objects.all()

        min_price, max_price = ProductModel.objects.aggregate(
            Min('real_price'),
            Max('real_price')
        ).values()

        context['min_price'], context['max_price'] = int(min_price), int(max_price)
        # context['min_price'], context['max_price'] = list(
        #     map(
        #         int,
        #         ProductModel.objects.aggregate(
        #             Min('real_price'),
        #             Max('real_price')
        #         ).values()
        #     )
        # )
        return context


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'shop-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = ProductModel.objects.filter(category=self.object.category).exclude(
            pk=self.object.pk)

        return context


class WishlistListView(LoginRequiredMixin, ListView):
    template_name = 'wishlist.html'

    def get_queryset(self):
        return self.request.user.wishlist.all()


class CartlistView(ListView):
    template_name = 'cart.html'

    def get_queryset(self):
        return ProductModel.get_from_cart(self.request)


@login_required
def add_wishlist(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    user = request.user
    if user in product.wishlist.all():
        product.wishlist.remove(user)
    else:
        product.wishlist.add(user)

    return redirect(request.GET.get('next', '/'))


def add_to_cart(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)
    request.session['cart'] = cart

    return redirect(request.GET.get('next', '/'))
