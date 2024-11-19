import base64

from django.core.files.base import ContentFile
from rest_framework import serializers

from content.models import New, Product, About


class Base64ImageField(serializers.ImageField):
    """Сериализатор для изображений."""

    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class NewSerializer(serializers.ModelSerializer):
    """Сериализатор модели New."""

    image = Base64ImageField(
        required=False,
        allow_null=True,

    )
    image_url = serializers.SerializerMethodField(
        'get_image_url'
    )

    class Meta:
        model = New
        fields = (
            'id',
            'name',
            'pub_date',
            'text',
            'image',
            'image_url'
        )

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Product."""

    preview = Base64ImageField(
        required=False,
        allow_null=True,
    )

    preview_url = serializers.SerializerMethodField(
        'get_preview_url'
    )

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'short_description',
            'description',
            'preview',
            'preview_url'
        )

    def get_preview_url(self, obj):
        if obj.preview:
            return obj.preview.url
        return None


class AboutSerializer(serializers.ModelSerializer):
    """Сериализатор модели с контактной информацией."""

    logo = Base64ImageField(
        required=False,
        allow_null=True,
    )

    logo_url = serializers.SerializerMethodField(
        'get_logo_url'
    )

    class Meta:
        model = About
        fields = (
            'id',
            'phone',
            'adress',
            'description',
            'logo',
            'logo_url'
        )

    def get_logo_url(self, obj):
        if obj.preview:
            return obj.logo.url
        return None
