from django.db import models


class New(models.Model):
    """Модель новости."""

    name = models.CharField(max_length=256)
    pub_date = models.DateTimeField('Дата выхода новости', auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(
        upload_to='content/news_images/',
        null=True,
        default=None
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара."""

    name = models.CharField(max_length=256)
    short_description = models.TextField(max_length=256)
    description = models.TextField
    preview = models.ImageField(
        upload_to='content/products_images',
        null=True,
        default=None
    )

    def __str__(self):
        return self.name


class About(models.Model):
    """Модель для контактной информации."""

    phone = models.TextField()
    email = models.EmailField()
    adress = models.TextField()
    description = models.TextField()
    logo = models.ImageField(
        default=0,
        null=False,
        blank=False
    )
