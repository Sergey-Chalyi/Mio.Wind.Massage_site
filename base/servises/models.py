from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва масажу")
    image = models.ImageField(upload_to='services/', verbose_name="Фотографія (дял картки)")
    short_description = models.TextField(verbose_name="Короткий опис")
    options = models.JSONField(verbose_name="Опції (тривалість, частини тіла та ціна) - JSON")
    show_on_main = models.BooleanField(default=False, verbose_name="Показувати на головній сторінці")
    show_on_all_servises = models.BooleanField(default=False, verbose_name="Показувати на сторінці зі всіма масажами")
    priority = models.PositiveIntegerField(verbose_name='Пріоритет картки (двозначним числом)', unique=True)

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Картка: послуга"
        verbose_name_plural = "Картки: послуги"

