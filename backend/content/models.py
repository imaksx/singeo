from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.core.files.storage import default_storage
from django.core.exceptions import ObjectDoesNotExist


class New(models.Model):
    """Модель новости."""

    name = models.CharField(max_length=256, verbose_name="Заголовок новости")
    pub_date = models.DateField(
        verbose_name="Дата выхода новости",
        auto_now_add=True,
    )
    text = models.TextField(verbose_name="Текст новости")
    video = models.FileField(
        upload_to="news_videos/",
        null=True,
        blank=True,
        verbose_name="Видео новости",
    )

    # Метод для ручного удаления видео
    def delete_video(self):
        if self.video:
            self.video.delete(save=False)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.name


# Сигнал для автоматического удаления видео при удалении новости
@receiver(pre_delete, sender=New)
def delete_news_video(sender, instance, **kwargs):
    instance.delete_video()


class NewsImage(models.Model):
    """Модель для изображений новостей."""

    news = models.ForeignKey(
        New,
        related_name="images",
        on_delete=models.CASCADE,
        verbose_name="Новость, которой назначается фотография",
    )
    image = models.ImageField(
        upload_to="news_images/", verbose_name="Фотография новости"
    )

    def delete_image(self):
        if self.image:
            self.image.delete(save=False)

    class Meta:
        verbose_name = "Изображение новости"
        verbose_name_plural = "Изображения новостей"


# Сигнал для автоматического удаления изображений при удалении новости
@receiver(pre_delete, sender=New)
def delete_news_images(sender, instance, **kwargs):
    # Удаляем все связанные изображения
    for image in instance.images.all():
        image.delete_image()
        image.delete()


class IndustryTag(models.Model):
    """Модель для тегов отраслей продуктов."""

    name = models.CharField(
        max_length=32,
        verbose_name="Название отрасли",
    )
    slug = models.SlugField(
        verbose_name="Slug отрасли (должен быть на английском языке)",
    )

    class Meta:
        verbose_name = "Отрасль для продуктов и проектов"
        verbose_name_plural = "Отрасли для продуктов и проектов"

    def __str__(self):
        return self.name


class ObjectTag(models.Model):
    """Модель для тегов объектов применения продуктов."""

    name = models.CharField(
        max_length=32,
        verbose_name="Название объекта применения",
    )
    slug = models.SlugField(
        verbose_name="Slug объекта применения (должен быть на английском языке)",
    )

    class Meta:
        verbose_name = "Объект применения для продуктов и проектов"
        verbose_name_plural = "Объекты применения для продуктов и проектов"

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара."""

    name = models.CharField(max_length=256, verbose_name="Название продукта")
    short_description = models.TextField(
        max_length=256, verbose_name="Краткое описание продукта"
    )
    description = models.TextField(verbose_name="Полное описание продукта")
    preview = models.ImageField(
        upload_to="products_images",
        null=True,
        default=None,
        verbose_name="Фотография продукта",
    )
    specifications = models.TextField(
        verbose_name="Основные технические характеристики", default=None
    )
    applying_objects = models.ManyToManyField(
        ObjectTag,
        related_name="products",
        verbose_name="Объекты применения",
        blank=True,
    )
    industries = models.ManyToManyField(
        IndustryTag,
        related_name="products",
        verbose_name="Отрасли",
        blank=True,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


# Сигнал для удаления медиа при удалении продукта
@receiver(pre_delete, sender=Product)
def delete_product_media(sender, instance, **kwargs):
    # Удаляем изображение
    if instance.preview:
        file_path = instance.preview.path
        if default_storage.exists(file_path):
            default_storage.delete(file_path)

    # Удаляем все связанные PDF-файлы
    for pdf in instance.pdfs.all():
        file_path = pdf.file.path
        if default_storage.exists(file_path):
            default_storage.delete(file_path)


# Сигнал для удаления медиа при обновлении продукта
@receiver(pre_save, sender=Product)
def update_product_media(sender, instance, **kwargs):
    # Получаем предыдущую версию объекта
    if instance.pk:
        try:
            old_instance = Product.objects.get(pk=instance.pk)

            # Проверяем и удаляем старое изображение
            if old_instance.preview and old_instance.preview != instance.preview:
                if default_storage.exists(old_instance.preview.path):
                    default_storage.delete(old_instance.preview.path)

            # Проверяем и удаляем старые PDF-файлы
            # Удаляем PDF-файлы, которые были удалены из связи
            old_pdf_ids = set(old_instance.pdfs.values_list("id", flat=True))
            new_pdf_ids = set(instance.pdfs.values_list("id", flat=True))
            removed_pdf_ids = old_pdf_ids - new_pdf_ids

            for pdf_id in removed_pdf_ids:
                try:
                    pdf = ProductPDF.objects.get(id=pdf_id)
                    file_path = pdf.file.path
                    if default_storage.exists(file_path):
                        default_storage.delete(file_path)
                except ProductPDF.DoesNotExist:
                    pass  # Если PDF-файл уже был удален другим процессом
        except ObjectDoesNotExist:
            pass  # Если старый объект не найден


class ProductPDF(models.Model):
    """Модель для хранения PDF-файлов, связанных с продуктом."""

    file = models.FileField(
        upload_to="pdfs/products/",
        verbose_name="Файл",
    )
    name = models.CharField(max_length=255, verbose_name="Название файла")
    product = models.ForeignKey(
        Product,
        related_name="pdfs",
        on_delete=models.CASCADE,
        verbose_name="Название продукта",
    )

    class Meta:
        verbose_name = "PDF-файл продукта"
        verbose_name_plural = "PDF-файлы продуктов"

    def __str__(self):
        return f"PDF Файл: {self.file.name} для продукта: {self.product.name}"


class Certificate(models.Model):
    """Модель для сертификатов."""

    image = models.ImageField(
        upload_to="certificates/", verbose_name="Изображение сертификата"
    )
    about = models.ForeignKey(
        "AboutIndex", related_name="certificates", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"


class AboutIndex(models.Model):
    """Модель для главной страницы, подвала и хедера."""

    phone = models.TextField(verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Адрес электронной почтой")
    address = models.TextField(default=None, verbose_name="Адрес предприятия")
    slogan = models.TextField(verbose_name="Слоган")
    description_1 = models.TextField(
        verbose_name="Описание 'О компании' для первого блока главной страницы"
    )
    description_2 = models.TextField(
        verbose_name="Описание 'О компании' для второго блока главной страницы"
    )

    def __str__(self):
        return "Модель для главной страницы"

    class Meta:
        verbose_name = "Наполнение главной страницы"
        verbose_name_plural = "Наполнение главной страницы (должно быть одно)"


class AboutCompany(models.Model):
    """Модель для раздела 'О нас'"""

    company_description = models.TextField(
        verbose_name="Текст с описанием компании в самом верху страницы"
    )
    colleagues_description = models.TextField(
        verbose_name="Текст для раздела 'Команда'", null=True
    )
    colleagues_main_image = models.ImageField(
        verbose_name="Общее фото для раздела 'Команда'",
        upload_to="company_image/",
        null=True,  # Добавляем возможность null для корректного удаления
        blank=True,
    )
    colleagues = models.ManyToManyField(
        "Colleague",
        related_name="companies",
        blank=True,
        verbose_name="Коллеги",
    )

    class Meta:
        verbose_name = "Наполнение раздела 'О нас'"
        verbose_name_plural = "Наполнение раздела 'О нас' (должно быть одно)"

    def __str__(self):
        return "О компании"


# Сигнал для автоматического удаления файла изображения при удалении AboutCompany
@receiver(pre_delete, sender=AboutCompany)
def delete_company_image(sender, instance, **kwargs):
    if instance.colleagues_main_image:
        instance.colleagues_main_image.delete(save=False)


class CompanyPDF(models.Model):
    """Модель для хранения PDF-файлов, связанных с компанией."""

    file = models.FileField(
        upload_to="pdfs/company/",
        verbose_name="PDF-файл",
    )
    name = models.CharField(max_length=255, verbose_name="Название файла")
    about_company = models.ForeignKey(
        "AboutCompany",
        related_name="pdfs",
        on_delete=models.CASCADE,
        verbose_name="Модель наполнения раздела 'О нас'",
    )

    class Meta:
        verbose_name = "PDF-файл компании"
        verbose_name_plural = "PDF-файлы компании"

    def __str__(self):
        return f"PDF Файл: {self.file.name}"


class LogoImage(models.Model):
    """Модель для логотипов компании-заказчика"""

    image = models.ImageField(
        upload_to="logo_images/",
        verbose_name="Логотип компании-заказчика",
    )
    about_company = models.ForeignKey(
        AboutCompany,
        related_name="logo_images",
        on_delete=models.CASCADE,
        verbose_name="Модель раздела 'О нас'",
    )

    class Meta:
        verbose_name = "Логотип компании-заказчика"
        verbose_name_plural = "Логотипы компаний-заказчиков"

    def __str__(self):
        return f"Логотип для {self.about_company}"


class Colleague(models.Model):
    """Модель для сотрудников компании"""

    name = models.CharField(max_length=255, verbose_name="Имя сотрудника")
    position = models.TextField(verbose_name="Должность")
    image = models.ImageField(
        upload_to="colleagues_images/", verbose_name="Фотография сотрудника"
    )

    class Meta:
        verbose_name = "Сотрудник компании"
        verbose_name_plural = "Сотрудники компании"

    def __str__(self):
        return self.name


# Сигнал для удаления файла изображения при удалении модели
@receiver(pre_delete, sender=Colleague)
def delete_colleague_image(sender, instance, **kwargs):
    # Проверяем, существует ли файл изображения
    if instance.image:
        # Получаем путь к файлу
        file_path = instance.image.path
        # Проверяем существование файла
        if default_storage.exists(file_path):
            # Удаляем файл
            default_storage.delete(file_path)


# Сигнал для удаления файла изображения при обновлении модели
@receiver(pre_save, sender=Colleague)
def update_colleague_image(sender, instance, **kwargs):
    # Получаем предыдущую версию объекта
    if instance.pk:
        try:
            old_instance = Colleague.objects.get(pk=instance.pk)
            # Если изображение изменилось, удаляем старое
            if old_instance.image and old_instance.image != instance.image:
                if default_storage.exists(old_instance.image.path):
                    default_storage.delete(old_instance.image.path)
        except Colleague.DoesNotExist:
            pass


class Region(models.Model):
    """Модель региона."""

    name = models.CharField(max_length=256, verbose_name="Название региона")
    is_active = models.BooleanField(
        default=False,
        verbose_name="Отображается на карте",
    )
    coord_x = models.FloatField(
        verbose_name="Координата X (долгота)",
        default=1.0,
    )
    coord_y = models.FloatField(
        verbose_name="Координата Y (широта)",
        default=1.0,
    )

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

    def __str__(self):
        return self.name


class Project(models.Model):
    """Модель проекта."""

    name = models.CharField(max_length=256, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание проекта")
    regions = models.ManyToManyField(
        Region, related_name="projects", verbose_name="Регионы проекта"
    )
    image = models.ImageField(
        upload_to="projects_images",
        null=True,
        blank=True,
        verbose_name="Фотография проекта",
    )
    location = models.TextField(
        null=True, blank=True, verbose_name="Город/точное местоположение"
    )
    related_products = models.ManyToManyField(
        "Product",
        through="ProjectProduct",
        verbose_name="Используемые продукты",
        blank=True,
    )
    tag_object = models.ManyToManyField(
        "ObjectTag",
        related_name="projects",
        verbose_name="Объект применения",
    )
    tag_sphere = models.ManyToManyField(
        "IndustryTag",
        related_name="projects",
        verbose_name="Отрасль",
    )

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name


class Map(models.Model):
    """Модель карты с активными регионами."""

    name = models.CharField(
        max_length=100, verbose_name="Название карты", default="Основная карта"
    )
    regions = models.ManyToManyField(
        Region,
        related_name="maps",
        verbose_name="Регионы на карте",
        limit_choices_to={"is_active": True},
        blank=True,
    )

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карта (должна быть одна)"

    def __str__(self):
        return self.name


class ProjectProduct(models.Model):
    """
    Промежуточная модель.
    Реализует отношение многие-ко-многим между
    продуктом и проектом.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Продукт в проекте"
        verbose_name_plural = "Продукты в проекте"

    def __str__(self):
        return f"Продукт '{self.product.name}' для проекта '{self.project.name}'"
