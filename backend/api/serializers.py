# import base64

# from datetime import datetime
# from django.core.files.base import ContentFile
# from rest_framework import serializers

# from content.models import New, Product, About, Project, ProjectProduct, ProjectRegion, Region, Map, MapRegion


# class Base64ImageField(serializers.ImageField):
#     """Сериализатор для изображений."""

#     def to_internal_value(self, data):
#         if isinstance(data, str) and data.startswith('data:image'):
#             format, imgstr = data.split(';base64,')
#             ext = format.split('/')[-1]

#             data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

#         return super().to_internal_value(data)


# class NewSerializer(serializers.ModelSerializer):
#     """Сериализатор модели New."""

#     image = Base64ImageField(
#         required=False,
#         allow_null=True,

#     )

#     def validate_pub_date(self, value):
#         """Приведение поля pub_date к виду день.месяц.год."""

#         try:
#             return datetime.strptime(value, '%d.%m.%Y').date()
#         except ValueError:
#             raise serializers.ValidationError(
#                 "Дата должна быть в формате день.месяц.год."
#             )

#     class Meta:
#         model = New
#         fields = (
#             'id',
#             'name',
#             'pub_date',
#             'text',
#             'image',
#         )


# class ProductSerializer(serializers.ModelSerializer):
#     """Сериализатор для модели Product."""

#     preview = Base64ImageField(
#         required=False,
#         allow_null=True,
#     )

#     class Meta:
#         model = Product
#         fields = (
#             'id',
#             'name',
#             'short_description',
#             'description',
#             'preview'
#         )


# class AboutSerializer(serializers.ModelSerializer):
#     """Сериализатор модели с контактной информацией."""

#     logo = Base64ImageField(
#         required=False,
#         allow_null=True,
#     )

#     class Meta:
#         model = About
#         fields = (
#             'id',
#             'phone',
#             'address',
#             'description',
#             'logo',
#         )


# class ProjectSerializer(serializers.ModelSerializer):
#     """Сериализатор модели проекта."""

#     image = Base64ImageField(
#         required=False,
#         allow_null=True,
#     )

#     class Meta:
#         model = Project
#         fields = (
#             'id',
#             'name',
#             'description',
#             'region',
#             'image',
#             'location',
#             'related_products',
#         )


# class RegionSerializer(serializers.ModelSerializer):
#     """Модель региона."""

#     class Meta:
#         model = Region
#         fields = (
#             'id',
#             'name',
#             'is_active',
#             'coords',
#         )
