from django.urls import path

from api.views import ProductListAPIView

app_name = 'api'

urlpatterns = [
    path('product/', ProductListAPIView.as_view())
]