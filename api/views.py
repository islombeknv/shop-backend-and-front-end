from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import ProductModelSerializer
from products.models import ProductModel


class ProductListAPIView(ListAPIView):
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()