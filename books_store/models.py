from django.db import models


class Book(models.Model):
    """Модель книги"""
    name = models.CharField("Название", max_length=20)
    title = models.CharField("Заголовок", max_length=30, null=True, blank=True)
    author = models.CharField("Автор", max_length=30)
    description = models.TextField("Описание", max_length=512, null=True, blank=True)
    price = models.PositiveSmallIntegerField("Цена", default=0, help_text='Обязательное поле', null=True, blank=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name


class Profile(models.Model):
    """Модель профиль"""
    column_name = models.CharField("Название столбца", max_length=20)
    is_visible = models.BooleanField("Видимость", default=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'

    def __str__(self):
        return self.column_name
