# Generated by Django 3.2 on 2024-12-15 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20241130_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Карта',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название проекта')),
                ('description', models.TextField(verbose_name='Описание проекта')),
                ('image', models.ImageField(default=None, null=True, upload_to='media/projects_images', verbose_name='Фотография проекта')),
                ('location', models.TextField(default=None, null=True, verbose_name='Город, более точное местоположение проекта.')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название региона')),
                ('is_active', models.BooleanField(default=False, verbose_name='Отображается на карте')),
                ('coords', models.CharField(max_length=256, verbose_name='Координаты для карты')),
            ],
            options={
                'verbose_name': 'Регионы',
            },
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.RemoveField(
            model_name='about',
            name='adress',
        ),
        migrations.AddField(
            model_name='about',
            name='address',
            field=models.TextField(default=None, verbose_name='Адрес предприятия'),
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(verbose_name="Описание 'О нас'"),
        ),
        migrations.AlterField(
            model_name='about',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Адрес электронной почтой'),
        ),
        migrations.AlterField(
            model_name='about',
            name='logo',
            field=models.ImageField(default=0, upload_to='', verbose_name='Изображение логотипа'),
        ),
        migrations.AlterField(
            model_name='about',
            name='phone',
            field=models.TextField(verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='media/news_images/', verbose_name='Фотография новости'),
        ),
        migrations.AlterField(
            model_name='new',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Заголовок новости'),
        ),
        migrations.AlterField(
            model_name='new',
            name='text',
            field=models.TextField(verbose_name='Текст новости'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Полное описание продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Название продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(default=None, null=True, upload_to='media/products_images', verbose_name='Фотография продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(max_length=256, verbose_name='Краткое описание продукта'),
        ),
        migrations.CreateModel(
            name='ProjectRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.project')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.region')),
            ],
            options={
                'verbose_name': 'Регионы проекта',
            },
        ),
        migrations.CreateModel(
            name='ProjectProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.product')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.project')),
            ],
            options={
                'verbose_name': 'Продукты в проекте',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='region',
            field=models.ManyToManyField(through='content.ProjectRegion', to='content.Region', verbose_name='Местоположение проекта'),
        ),
        migrations.AddField(
            model_name='project',
            name='related_products',
            field=models.ManyToManyField(through='content.ProjectProduct', to='content.Product', verbose_name='Продукты, используемые в проекте'),
        ),
        migrations.CreateModel(
            name='MapRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.map')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.region')),
            ],
            options={
                'verbose_name': 'Регионы на карте',
            },
        ),
        migrations.AddField(
            model_name='map',
            name='regions',
            field=models.ManyToManyField(through='content.MapRegion', to='content.Region', verbose_name='Регионы на карте'),
        ),
    ]