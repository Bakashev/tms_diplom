from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Модель пользователя с доплнительными полями расширяющие базовую модель
    """
    address = models.CharField(max_length=250)
    balance = models.FloatField(default=0.0)
    phone = models.CharField(max_length=13)
    organization = models.CharField(max_length=250)

    class Meta:
        db_table = 'user'
