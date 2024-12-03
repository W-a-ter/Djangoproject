from django.db import models

# Create your models here.


class Category(models.Model):
    """Модель создания таблицы в БД Категория"""

    objects = None
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.CharField(max_length=500, verbose_name="Описание", null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель создания таблицы в БД Продукты"""

    objects = None
    name = models.CharField(max_length=150, verbose_name="Наименование")  # столбцы таблицы
    description = models.CharField(max_length=500, verbose_name="Описание", null=True)
    picture = models.ImageField(upload_to="catalog/photo/", verbose_name="Изображение", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров", help_text="Укажите количество просмотров", default=0, editable=False)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_at"]

    def __str__(self):
        return f"{self.name} - {self.price}"
