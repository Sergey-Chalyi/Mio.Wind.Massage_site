from django.db import models

class Logo(models.Model):
    text = models.CharField(max_length=100, verbose_name="Назва компанії")
    icon_main = models.FileField(upload_to='blocks/', verbose_name="Логотип для відображення на сайті")
    icon_flavic = models.FileField(upload_to='blocks/', verbose_name="Логотип для відображення на вкладках")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')
    

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = "Секція: логотипи"
        verbose_name_plural = "Секція: логотипи"


class CompanySocials(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва мережі", blank=True)
    link = models.CharField(max_length=255, verbose_name="Посилання", blank=True)
    icon = models.FileField(upload_to='socials/', blank=True, verbose_name="Іконка")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Секція: соціальні мережі компанії"
        verbose_name_plural = "Секція: соціальні мережі компанії"
    


class WelcomeBlock(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва поля на сайті", blank=True)
    text = models.CharField(max_length=100, verbose_name="Текст", blank=True)
    photo = models.ImageField(upload_to='blocks/', blank=True, verbose_name="Фото (ЛИШЕ ДЛЯ company_photo)")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Секція: вітальна"
        verbose_name_plural = "Секція: вітальна"


class GenInfoBlock(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.CharField(max_length=100, verbose_name="Текст")
    icon = models.FileField(upload_to='blocks/', verbose_name="Іконка")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Секція: загальна інформація"
        verbose_name_plural = "Секція: загальна інформація"


class AboutAsBlock(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва поля на сайті")
    text = models.TextField(verbose_name="Опис компанії")
    photo_full = models.ImageField(upload_to='blocks/', verbose_name="Фото для повного екрану")
    photo_short = models.ImageField(upload_to='blocks/', verbose_name="Фото для вузького екрану")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Секція: про нас"
        verbose_name_plural = "Секція: про нас"


class GeneralBenefitsBlock(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    icon = models.FileField(upload_to='blocks/', verbose_name="Іконка")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Секція: загальні переваги"
        verbose_name_plural = "Секція: загальні переваги"


class AdvantagesBlock(models.Model):
    title = models.CharField(max_length=10, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Секція: переваги"
        verbose_name_plural = "Секція: переваги"


class FooterBlock(models.Model):
    title = models.CharField(max_length=255, verbose_name="Усі права захищені")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Секція: футер"
        verbose_name_plural = "Секція: футер"


class FAQ(models.Model):
    title = models.TextField(verbose_name="Запитання")
    description = models.TextField(verbose_name="Відповідь")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Секція: часті запитання"
        verbose_name_plural = "Секція: часті запитання"


class PrivacyPolicy(models.Model):
    text = models.TextField(verbose_name="Політика конфіденційності")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')
    

    def __str__(self):
        return f'{self.text[:100]}...'
    
    class Meta:
        verbose_name = "Секція: політика конфіденційності"
        verbose_name_plural = "Секція: політика конфіденційності"


class OtherPagesMainPhotos(models.Model):
    page_name = models.CharField(max_length=100, verbose_name="Назва сторінки")
    title = models.CharField(max_length=255, verbose_name="Фраза зверху сторінки")
    photo = models.ImageField(upload_to='pictures/', verbose_name="Фото для верху сторінки")

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')
    

    def __str__(self):
        return self.page_name
    
    class Meta:
        verbose_name = "Секція: фото для сторінок"
        verbose_name_plural = "Секція: фото для сторінок"


class VisitRecord(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name="Ім'я клієнта")
    customer_tel = models.CharField(max_length=100, verbose_name="Номер клієнта")
    customer_comment = models.TextField(max_length=1000, verbose_name="Коментар клієнта", blank=True)

    to_specialist = models.CharField(max_length=100, verbose_name="До спеціаліста", blank=True)
    servise_name = models.CharField(max_length=100, verbose_name="Назва послуги", blank=True)
    servise_duration = models.CharField(max_length=100, verbose_name="Тривалість послуги", blank=True)
    servise_count = models.CharField(max_length=100, verbose_name="Кількість послуг", blank=True)
    
    is_processed = models.BooleanField(default=False, verbose_name='Чи клієнт обслугований?')

    time_created = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Дата створення')
    time_updated = models.DateTimeField(blank=True, auto_now=True, verbose_name='Дата редагування')
    

    def __str__(self):
        return f'{self.time_created.day}/{self.time_created.month}/{self.time_created.year}_{self.customer_name}'
    
    class Meta:
        verbose_name = "ІНФОРМАЦІЯ: Запис клієнта"
        verbose_name_plural = "ІНФОРМАЦІЯ: Записи клієнтів"



