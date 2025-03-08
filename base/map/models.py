from django.db import models

class MapPageInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва блоку")
    photo = models.FileField(upload_to='maps/', verbose_name="Фото дорожньої карти здоров'я")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Секція: карта здоров'я"
        verbose_name_plural = "Секція: карта здоров'я"