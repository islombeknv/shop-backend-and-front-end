from django.urls import path

from api.views import ProductListAPIView, ProductRetrieveAPIView

app_name = 'api'

urlpatterns = [
    path('product/', ProductListAPIView.as_view()),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view()),
]