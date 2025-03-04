# Generated by Django 3.2 on 2025-03-02 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_aboutcompany_colleagues'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colleague',
            name='about_company',
        ),
        migrations.AlterField(
            model_name='about',
            name='description_1',
            field=models.TextField(verbose_name="Описание 'О компании' для первого блока главной страницы"),
        ),
        migrations.AlterField(
            model_name='about',
            name='description_2',
            field=models.TextField(verbose_name="Описание 'О компании' для второго блока главной страницы"),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='colleagues',
            field=models.ManyToManyField(blank=True, related_name='companies', to='content.Colleague', verbose_name='Коллеги'),
        ),
    ]
