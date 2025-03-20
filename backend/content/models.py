from django.db import models


class New(models.Model):
    """Модель новости."""
    name = models.CharField(max_length=256, verbose_name='Заголовок новости')
    pub_date = models.DateField(
        verbose_name='Дата выхода новости', auto_now_add=True)
    text = models.TextField(verbose_name='Текст новости')
    video = models.FileField(upload_to='news_videos/',
                             null=True, blank=True, verbose_name='Видео новости')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.name


class NewsImage(models.Model):
    """Модель для изображений новостей."""
    news = models.ForeignKey(New, related_name='images',
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/',
                              verbose_name='Фотография новости')

    class Meta:
        verbose_name = 'Изображение новости'
        verbose_name_plural = 'Изображения новостей'


class TechnicalDescription(models.Model):
    """Модель для основных характеристик продукта."""

    product = models.ForeignKey(
        'Product', related_name='technical_descriptions', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Основная характеристика')

    def __str__(self):
        return self.description


class Product(models.Model):
    """Модель товара."""

    name = models.CharField(
        max_length=256,
        verbose_name='Название продукта')
    short_description = models.TextField(
        max_length=256,
        verbose_name='Краткое описание продукта')
    description = models.TextField(
        verbose_name='Полное описание продукта')
    preview = models.ImageField(
        upload_to='products_images',
        null=True,
        default=None,
        verbose_name='Фотография продукта')
    specifications = models.TextField(
        verbose_name='Основные технические характеристики',
        default=None
    )
    applying_object = models.TextField(
        verbose_name='Объект применения',
        default=None
    )
    sphere = models.TextField(
        verbose_name='Отрасль',
        default=None
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class ProductPDF(models.Model):
    """Модель для хранения PDF-файлов, связанных с продуктом."""
    file = models.FileField(upload_to='pdfs/products/')
    name = models.CharField(max_length=255, verbose_name='Название файла')
    product = models.ForeignKey(
        Product,
        related_name='pdfs',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'PDF файл продукта'
        verbose_name_plural = 'PDF файлы продуктов'

    def __str__(self):
        return f"PDF Файл: {self.file.name} для продукта: {self.product.name}"


class Certificate(models.Model):
    """Модель для сертификатов."""

    image = models.ImageField(
        upload_to='certificates/',
        verbose_name='Изображение сертификата')
    about = models.ForeignKey(
        'AboutIndex',
        related_name='certificates',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class AboutIndex(models.Model):
    """Модель для главной страницы, подвала и хедера."""

    phone = models.TextField(
        verbose_name='Номер телефона')
    email = models.EmailField(
        verbose_name='Адрес электронной почтой')
    address = models.TextField(
        default=None,
        verbose_name='Адрес предприятия')
    slogan = models.TextField(
        verbose_name="Слоган")
    description_1 = models.TextField(
        verbose_name="Описание 'О компании' для первого блока главной страницы")
    description_2 = models.TextField(
        verbose_name="Описание 'О компании' для второго блока главной страницы")

    class Meta:
        verbose_name = 'Модель для главной страницы'
        verbose_name_plural = 'Модели для главной страницы'


class AboutCompany(models.Model):
    """Модель для раздела 'О нас'"""

    company_description = models.TextField(
        verbose_name='Текст с описанием компании в самом верху страницы'
    )
    colleagues_description = models.TextField(
        verbose_name="Текст для раздела 'Команда'",
        null=True
    )
    colleagues_main_image = models.ImageField(
        verbose_name="Общее фото для раздела 'Команда'",
        upload_to='company_image/',
    )
    colleagues = models.ManyToManyField(
        'Colleague',
        related_name='companies',
        blank=True,
        verbose_name='Коллеги',
    )

    def __str__(self):
        return "О компании"


class CompanyPDF(models.Model):
    """Модель для хранения PDF-файлов, связанных с компанией."""
    file = models.FileField(upload_to='pdfs/company/')
    name = models.CharField(max_length=255, verbose_name='Название файла')
    about_company = models.ForeignKey(
        'AboutCompany',
        related_name='pdfs',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"PDF Файл: {self.file.name}"


class LogoImage(models.Model):
    """Модель для логотипов компании"""
    image = models.ImageField(upload_to='logo_images/',
                              verbose_name='Логотип компании')
    about_company = models.ForeignKey(
        AboutCompany,
        related_name='logo_images',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Логотип для {self.about_company}"


class Colleague(models.Model):
    """Модель для коллег компании"""

    name = models.CharField(max_length=255, verbose_name='Имя коллеги')
    position = models.TextField(verbose_name='Должность')
    image = models.ImageField(upload_to='colleagues_images/',
                              verbose_name='Фотография коллеги')

    def __str__(self):
        return self.name


class Region(models.Model):
    """Модель региона."""

    name = models.CharField(
        max_length=256,
        verbose_name='Название региона')
    is_active = models.BooleanField(
        default=False,
        verbose_name='Отображается на карте')
    # нужен валидатор
    coords = models.CharField(
        max_length=256,
        verbose_name='Координаты регионального центра.')

    class Meta:
        verbose_name = 'Регионы'
        verbose_name = 'Регионы'

    def __str__(self):
        return self.name


class Project(models.Model):
    """Модель проекта."""

    name = models.CharField(
        max_length=256,
        verbose_name='Название проекта')
    description = models.TextField(
        verbose_name='Описание проекта')
    region = models.ManyToManyField(
        Region,
        through='ProjectRegion',
        verbose_name='Местоположение проекта')
    image = models.ImageField(
        upload_to='projects_images',
        null=True,
        default=None,
        verbose_name='Фотография проекта')
    location = models.TextField(
        null=True,
        default=None,
        verbose_name='Город, более точное местоположение проекта.',)
    related_products = models.ManyToManyField(
        Product,
        through='ProjectProduct',
        verbose_name='Продукты, используемые в проекте',
        blank=False)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class TagForProject(models.Model):
    """Модель объектов для товара."""
    # ПОКА НИКУДА НЕ ПОДКЛЮЧЕН
    name = models.CharField(
        max_length=32,
        verbose_name='Название отрасли')
    slug = models.SlugField(
        verbose_name='project_slug')

    class Meta:
        verbose_name = 'Тег для проекта'
        verbose_name_plural = 'Теги для проекта'


class Map(models.Model):
    """Модель карты."""

    regions = models.ManyToManyField(
        Region,
        through='MapRegion',
        verbose_name='Регионы на карте')

    class Meta:
        verbose_name = 'Карта'


class ProjectProduct(models.Model):
    """
    Промежуточная модель.
    Реализует отношение многие-ко-многим между
    продуктом и проектом.
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт в проекте'
        verbose_name = 'Продукты в проекте'


class ProjectRegion(models.Model):
    """
    Промежуточная модель.
    Реализует отношение многие-ко-многим между
    проектом и регионом.
    """

    region = models.ForeignKey(
        Region, on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Регион проекта'
        verbose_name = 'Регионы проекта'


class MapRegion(models.Model):
    """
    Промежуточная модель.
    Реализует отношение многие-ко-многим между
    картой и регионом.
    """

    region = models.ForeignKey(
        Region, on_delete=models.CASCADE)
    Map = models.ForeignKey(
        Map, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Регион на карте'
        verbose_name = 'Регионы на карте'
