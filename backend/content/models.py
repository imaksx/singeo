from django.db import models


class New(models.Model):
    """Модель новости."""

    name = models.CharField(
        max_length=256,
        verbose_name='Заголовок новости'
    )
    pub_date = models.DateField(
        verbose_name='Дата выхода новости',
        auto_now_add=True,
    )
    text = models.TextField(
        verbose_name='Текст новости',
    )
    image = models.ImageField(
        upload_to='news_images/',
        null=True,
        default=None,
        verbose_name='Фотография новости'
    )

    video = models.FileField(  # Поле для видео
        upload_to='news_videos/',
        null=True,
        blank=True,  # Позволяет оставлять поле пустым
        verbose_name='Видео новости'
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.name


class TagForProduct(models.Model):
    """Модель объектов для товара."""

    name = models.CharField(
        max_length=32,
        verbose_name='Название объекта применения'
    )

    slug = models.SlugField(
        verbose_name='product_slug'
    )

    class Meta:
        verbose_name = 'Тег для товара'
        verbose_name_plural = 'Теги для товара'

    def __str__(self):
        return self.name


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
        verbose_name='Название продукта'
    )
    short_description = models.TextField(
        max_length=256,
        verbose_name='Краткое описание продукта'
    )
    description = models.TextField(
        verbose_name='Полное описание продукта'
    )
    preview = models.ImageField(
        upload_to='products_images',
        null=True,
        default=None,
        verbose_name='Фотография продукта'
    )
    tags = models.ManyToManyField(
        TagForProduct,
        related_name='products',
        blank=True,
        verbose_name='Теги для продукта'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class TagProduct(models.Model):
    """Промежуточная модель для товара и тега."""

    product_tag = models.ForeignKey(
        TagForProduct,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product_tag', 'product'],
                                    name='unique_tagproduct')
        ]
        verbose_name = 'Тег товара'
        verbose_name_plural = 'Теги товара'

    def __str__(self):
        """Метод строкового представления модели."""

        return f'{self.product_tag} {self.product}'


class Certificate(models.Model):
    """Модель для сертификатов."""
    image = models.ImageField(
        upload_to='certificates/',  # Папка для хранения изображений сертификатов
        verbose_name='Изображение сертификата'
    )
    about = models.ForeignKey(
        'About',
        related_name='certificates',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class About(models.Model):
    """Модель для контактной информации."""

    phone = models.TextField(
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почтой'
    )
    address = models.TextField(
        default=None,
        verbose_name='Адрес предприятия'
    )

    slogan = models.TextField(
        verbose_name="Слоган"
    )

    description_1 = models.TextField(
        verbose_name="Описание 'О нас' для первого блока"
    )

    description_2 = models.TextField(
        verbose_name="Описание 'О нас' для второго блока"
    )

    class Meta:
        verbose_name = 'О нас'


class Region(models.Model):
    """Модель региона."""

    name = models.CharField(
        max_length=256,
        verbose_name='Название региона'
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Отображается на карте'
    )
    # нужен валидатор
    coords = models.CharField(
        max_length=256,
        verbose_name='Координаты регионального центра.'
    )

    class Meta:
        verbose_name = 'Регионы'
        verbose_name = 'Регионы'

    def __str__(self):
        return self.name


class Project(models.Model):
    """Модель проекта."""

    name = models.CharField(
        max_length=256,
        verbose_name='Название проекта'
    )
    description = models.TextField(
        verbose_name='Описание проекта'
    )
    region = models.ManyToManyField(
        Region,
        through='ProjectRegion',
        verbose_name='Местоположение проекта'
    )
    image = models.ImageField(
        upload_to='projects_images',
        null=True,
        default=None,
        verbose_name='Фотография проекта'
    )
    location = models.TextField(
        null=True,
        default=None,
        verbose_name='Город, более точное местоположение проекта.',
    )
    related_products = models.ManyToManyField(
        Product,
        through='ProjectProduct',
        verbose_name='Продукты, используемые в проекте',
        blank=False
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class TagForProject(models.Model):
    """Модель объектов для товара."""

    name = models.CharField(
        max_length=32,
        verbose_name='Название отрасли'
    )

    slug = models.SlugField(
        verbose_name='project_slug'
    )

    class Meta:
        verbose_name = 'Тег для проекта'
        verbose_name_plural = 'Теги для проекта'


class TagProduct(models.Model):
    """Промежуточная модель для проекта и тега."""

    project_tag = models.ForeignKey(
        TagForProduct,
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project_tag', 'project'],
                                    name='unique_tagproject')
        ]
        verbose_name = 'Тег товара'
        verbose_name_plural = 'Теги товара'

    def __str__(self):
        """Метод строкового представления модели."""

        return f'{self.project_tag} {self.project}'


class Map(models.Model):
    """Модель карты."""

    regions = models.ManyToManyField(
        Region,
        through='MapRegion',
        verbose_name='Регионы на карте'
    )

    class Meta:
        verbose_name = 'Карта'


class ProjectProduct(models.Model):
    """
    Промежуточная модель.
    Реализует отношение многие-ко-многим между
    продуктом и проектом.
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )

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
        Region, on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )

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
        Region, on_delete=models.CASCADE
    )
    Map = models.ForeignKey(
        Map, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Регион на карте'
        verbose_name = 'Регионы на карте'
