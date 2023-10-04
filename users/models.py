from django.db import models
from django.contrib.auth.models import AbstractUser
from logistic.models import BalanceOperation
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

    def user_balance(self):

        balances = BalanceOperation.objects.filter(user_id=self.pk)
        self.balance = 0
        for balnce in balances:
            self.balance += balnce.sum
        self.save()
