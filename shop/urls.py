from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    path('accounts/', include('auth.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='products')),
    path('blog/', include('posts.urls', namespace='posts')),
    path('profile/', include('users.urls', namespace='profile')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('api/', include('api.urls', namespace='api')),
    path('', include('pages.urls', namespace='pages')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
