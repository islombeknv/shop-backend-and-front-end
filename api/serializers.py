from rest_framework import serializers

from products.models import ProductModel, SizeModel, BrandModel, ColorModel, CategoryModel, ProductTagModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        exclude = [
            'title_ru',
            'title_uz',
            'title_en',
        ]


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'


class SizeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeModel
        fields = '__all__'


class ColorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = '__all__'


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTagModel
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    brand = BrandModelSerializer()
    colors = ColorModelSerializer(many=True)
    sizes = SizeModelSerializer(many=True)
    tags = TagModelSerializer(many=True)

    class Meta:
        model = ProductModel
        exclude = [
            'title_uz',
            'title_ru',
            'title_en',
            'short_description_ru',
            'short_description_uz',
            'short_description_en',
            'long_description_ru',
            'long_description_uz',
            'long_description_en',
            'wishlist',
        ]
