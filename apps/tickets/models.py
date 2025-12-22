from django.db import models
from django.conf import settings


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статуси'


class Ticket(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва тікету')
    description = models.TextField(verbose_name='Опис тікету')
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Ініціатор',
        related_name='author'
    )
    executor = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Виковавець',
        related_name='executor'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        to=Status,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='status',
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Тікет'
        verbose_name_plural = 'Тікети'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
