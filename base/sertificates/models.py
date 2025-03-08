from tokenize import Comment
from django.db import models
from servises.models import Service
from django.core.exceptions import ValidationError



class SubscriptionsPageinfo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва блоку")
    text = models.TextField(verbose_name="Текст", blank=True)
    photo = models.FileField(upload_to='backgrounds/', verbose_name='Фото для фону', blank=True)

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Секція: абонементи"
        verbose_name_plural = "Секції: абонементи"


class Subscription(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва абонемента")
    
    photo = models.ImageField(upload_to="subscriptions/", blank=True, null=True, verbose_name="Фото для картки (нормальної по ширині)")
    photo_short = models.ImageField(upload_to="subscriptions/", blank=True, null=True, verbose_name="Фото для картки (для вузьких екранів)")
    
    phrase = models.CharField(max_length=255, verbose_name="Прикольна фраза")
    durations = models.JSONField(verbose_name="Види абонементів по тривалості (JSON)")
    counts = models.JSONField(verbose_name="Види абонементів по кількості (JSON)")

    discount_info = models.CharField(max_length=50, blank=True, verbose_name="Додаткова інформація про знижку")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Картка: абонемент"
        verbose_name_plural = "Картки: абонементи"
    

class SertificatesPageinfo(models.Model):
    background = models.FileField(upload_to='backgrounds/', verbose_name='Картинка для фону')

    phrase_for_servise_sertificate = models.TextField(verbose_name="Прикольна фраза для сертифіката на послугу")
    phrase_for_sum_sertificate = models.TextField(verbose_name="Прикольна фраза для сертифіката на суму")

    description_for_servise_sertificate = models.TextField(verbose_name="Опис для сертифікату на послугу")
    description_for_sum_sertificate = models.TextField(verbose_name="Опис для сертифікату на суму")

    popular_servises = models.ManyToManyField(Service, verbose_name="Популярні послуги (ОБРАТИ РІВНО 3)")

    photo_for_servise_sertificate = models.FileField(upload_to='cards/', verbose_name='Картинка для сертифікату на послугу')
    photo_for_sum_sertificate = models.FileField(upload_to='cards/', verbose_name='Картинка для сертифікату на суму')

    comment_for_sum_sertificate  = models.TextField(verbose_name="Коментар (*...)", blank=True)

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')


    def clean(self):
        super().clean()
        if self.id and self.popular_servises.count() != 3:
            raise ValidationError("Виберіть рівно 3 популярні послуги.")
    
    def __str__(self):
        return self.phrase_for_servise_sertificate[:10] + '...'
    
    class Meta:
        verbose_name = "Секція: сертифікати"
        verbose_name_plural = "Секція: сертифікати"


class SertificateForSum(models.Model):
    price = models.FloatField(verbose_name='Ціна')
    
    photo = models.ImageField(upload_to="subscriptions/", blank=True, null=True, verbose_name="Фото (нормальне по ширині)")
    photo_short = models.ImageField(upload_to="subscriptions/", blank=True, null=True, verbose_name="Фото (для вузьких екранів)")

    altedgio_url = models.URLField(verbose_name="Посилання на відгуки Альтеджио", blank=True, null=True)

    phrase = models.CharField(max_length=255, verbose_name="Фраза")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = "Картка: сертифікат на суму"
        verbose_name_plural = "Картки: cертифікати на суму"
