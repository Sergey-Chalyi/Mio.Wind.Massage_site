from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

from servises.models import Service


class EmployeesPageInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва блоку")
    text = models.TextField(verbose_name="Текст")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Секція: спеціалісти"
        verbose_name_plural = "Секція: спеціалісти"


class Employee(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ім'я")
    last_name = models.CharField(max_length=100, verbose_name="Прізвище")
    middle_name = models.CharField(max_length=100, verbose_name="По батькові")

    main_photo = models.ImageField(upload_to='employees/', 
    blank=True, verbose_name="Головне фото")
    card_photo = models.ImageField(upload_to='employees/', 
    blank=True, verbose_name="Фото для картки")
    ava_photo = models.ImageField(upload_to='employees/', 
    blank=True, verbose_name="Фото для аватарки")

    specialization_short = models.CharField(max_length=255, verbose_name="Спеціалізація (коротко)")
    specialization_detailed = models.TextField(verbose_name="Спеціалізація (детально)")
    short_description = models.TextField(verbose_name="Короткий опис")

    work_experience = models.FloatField(verbose_name="Досвід роботи (у роках)")
    education = models.TextField(verbose_name="Освіта")
    scientific_activity = models.JSONField(verbose_name="Наукова діяльність (JSON)", blank=True, null=True)
    professional_pathways = models.TextField(verbose_name="Шляхи професійного розвитку", blank=True, null=True)

    services = models.ManyToManyField(Service, related_name='employees', verbose_name="Послуги (можна обирати декілька)")

    hobbies_and_interests = models.TextField(verbose_name="Хобі, улюблені фільми, книги", blank=True, null=True)
    doctor_advice = models.TextField(verbose_name="Поради від лікаря", blank=True, null=True)

    altedgio_reviews_url = models.URLField(verbose_name="Посилання на відгуки в Альтеджіо", blank=True, null=True)
    altedgio_booking_url = models.URLField(verbose_name="Посилання на запис в Альтеджіо", blank=True, null=True)
    telegram_url = models.URLField(verbose_name="Посилання на Telegram", blank=True, null=True)
    instagram_url = models.URLField(verbose_name="Посилання на Instagram", blank=True, null=True)

    is_active = models.BooleanField(default=True, verbose_name="Чи працює")
    show_on_homepage = models.BooleanField(default=False, verbose_name="Показувати на головній сторінці")
    show_on_all_specialists = models.BooleanField(default=True, verbose_name="Показувати на сторінці зі всіма масажистами")

    priority = models.PositiveIntegerField(verbose_name='Пріоритет картки (двозначним числом)', unique=True)
    stars_count = models.PositiveIntegerField(
        verbose_name='Кількість зірок',
        validators=[
            MinValueValidator(1, message="Кількість зірок має бути не менше 1."),
            MaxValueValidator(5, message="Кількість зірок має бути не більше 5.")
        ]
    )
    feedbacks_count = models.CharField(max_length=50, verbose_name='Кількість відгуків (наприклад: "38 відгуків")')

    slug = models.SlugField(unique=True, db_index=True, verbose_name="Слаг")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.pk}_{self.first_name}_{self.last_name}")
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
    class Meta:
        verbose_name = "Картка: співробітник"
        verbose_name_plural = "Картки: співробітники"



class Comment(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ім'я")
    last_name = models.CharField(max_length=100, verbose_name="Прізвище", blank=True)
    middle_name = models.CharField(max_length=100, verbose_name="По батькові", blank=True)

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')

    stars_count = models.PositiveIntegerField(
        verbose_name='Кількість зірок',
        validators=[
            MinValueValidator(1, message="Кількість зірок має бути не менше 1."),
            MaxValueValidator(5, message="Кількість зірок має бути не більше 5.")
        ]
    )

    specialist = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name='comments', verbose_name='Спеціаліст')

    text = models.TextField(max_length=320, verbose_name='Відгук')

    show_on_homepage = models.BooleanField(default=False, verbose_name="Показувати на головній сторінці")


    def __str__(self):
        return f"{self.first_name}_{self.time_created.year}"
    
    class Meta:
        verbose_name = "Картка: відгук"
        verbose_name_plural = "Картки: відгуки"