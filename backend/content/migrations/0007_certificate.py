# Generated by Django 3.2 on 2025-01-18 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20250118_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='certificates/', verbose_name='Изображение сертификата')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='content.about')),
            ],
            options={
                'verbose_name': 'Сертификат',
                'verbose_name_plural': 'Сертификаты',
            },
        ),
    ]
