import datetime
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diplom.settings')
django.setup()

from django.db.models import Count, Max
from logistic.models import Order, Services, PlaceDelivery, BalanceOperation, Correspondence


"""Запрос для получения всех заказов"""
# all_order = Order.objects.all()
# print(all_order.query)
# print(all_order)

"""Отображает перечень всех сервисов"""
# all_service = Services.objects.all()
# print(all_service)

#order = Order.objects.filter(id=10)
# service = Order.objects.get(id=30).service.all()
#
# #print(order)
# print(service.values_list())
# count_service = 0
# for i in service:
#     print(i.ser_price)
#     count_service += i.ser_price
# print(count_service)


# services = Services.objects.filter()
# delivery = Order.objects.filter(id=1)
# for i in delivery:
#     print(i.place_delivery.pd_price)


#Вывод всех операций пользователя
# balance = BalanceOperation.objects.filter(user_id=2)
# print(balance)

# Вывод комментарии заказа
corr = Correspondence.objects.select_related("order_id").filter(order_id=12)
print(corr)
