from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Назва посади')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Посада'
        verbose_name_plural = 'Посади'


class CustomManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('Вкажіть логін користувача !')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Для супер користувача параметр is_staff має бути True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Для супер користувача параметр is_superuser має бути True.')

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    first_name = None
    last_name = None

    username = models.CharField(max_length=32, unique=True, verbose_name='Логін')
    name = models.CharField(max_length=64, verbose_name='ПІБ користувача')
    email = models.EmailField(max_length=255, unique=True, verbose_name='ПІБ користувача')
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Посада')
    is_active = models.BooleanField(default=True, verbose_name='Активний обліковий запис')

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    objects = CustomManager()
