# Generated by Django 3.2 on 2025-01-18 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20250109_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='products', to='content.TagForProduct', verbose_name='Теги для продукта'),
        ),
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='news_images/', verbose_name='Фотография новости'),
        ),
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(default=None, null=True, upload_to='products_images', verbose_name='Фотография продукта'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='projects_images', verbose_name='Фотография проекта'),
        ),
    ]
