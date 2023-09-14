import datetime
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diplom.settings')
django.setup()

from django.db.models import Count, Max
from logistic.models import Order, Services


"""Запрос для получения всех заказов"""
all_order = Order.objects.all()
print(all_order.query)
print(all_order)

"""Отображает перечень всех сервисов"""
all_service = Services.objects.all()
print(all_service)