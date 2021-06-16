from django.urls import path

from products.views import ProductlistView, ProductDetailView, WishlistListView, add_wishlist, add_to_cart, CartlistView

app_name = 'products'

urlpatterns = [
    path('', ProductlistView.as_view(), name='list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('products/<int:pk>/', ProductlistView.as_view(), name='category'),
    path('wishlist/', WishlistListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', add_wishlist, name='add-wishlist'),
    path('cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('cart/', CartlistView.as_view(), name='cart_list'),
]