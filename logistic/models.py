from django.db import models


class Order(models.Model):
    """ Модель карточки заказа"""
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='order')
    city_auction = models.ForeignKey('CityAuction', on_delete=models.CASCADE, related_name='city')
    name_auction = models.CharField(max_length=250)
    address_auction = models.CharField(max_length=250)
    number_order = models.IntegerField()
    model_transport = models.CharField(max_length=250)
    description = models.TextField()
    place_delivery = models.ForeignKey('PlaceDelivery', on_delete=models.CASCADE, related_name='delivery')
    transportation = models.ForeignKey('Transportation', on_delete=models.CASCADE, related_name='transport')
    correspondence = models.TextField()
    service = models.ManyToManyField('Services')
    photo = models.ImageField(upload_to='image', default=None, null=True,  blank=False)
    price = models.FloatField(default=0)

    class Meta:
        db_table = 'order'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def calculated_price(self):
        """
        Функция для расчета цены

        """
        order_id = self.id
        services = Order.objects.get(id=self.id).service.all()
        print(order_id)
        count_service = 0
        # Расчет стоимости услуг
        for service in services:
            count_service += service.ser_price
            print(count_service)
        # Расчет стоимости услуг с учетом места отпрвки
        delivery = Order.objects.filter(id=self.id)
        for val in delivery:
            count_service += val.place_delivery.pd_price

        # Расчет стоимости услуг с учетом типа транспортировки
        transportation = Order.objects.filter(id=self.id)
        for val in transportation:
            count_service += val.transportation.tr_price

        return count_service

class Correspondence(models.Model):
    """Модель для хранения переписки в рамках заказа"""
    message = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='correspond')
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_core')

    class Meta:
        db_table = 'correspondence'


class BalanceOperation(models.Model):
    """Модель для хранения истории поплнения баланса"""

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    sum = models.FloatField()
    date_operation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'balanceoperation'






class CityAuction(models.Model):
    """Модель для хранения перечня городов с которыми работает система"""
    city_name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.city_name}'

    class Meta:
        db_table = 'cityauction'


class PlaceDelivery(models.Model):
    """Модель для хранения пунктов доставки до которых может быть доставлено ТС"""
    pd_name = models.CharField(max_length=250)
    pd_address = models.CharField(max_length=250)
    pd_price = models.FloatField()

    def __str__(self):
        return f'{self.pd_name}'
    class Meta:
        db_table = 'placedelivery'


class Transportation(models.Model):
    """Модель для хранения вариантов транспортировки"""
    tr_name = models.CharField(max_length=250)
    type_transport = models.CharField(max_length=250)
    tr_price = models.FloatField()

    def __str__(self):
        return f"{self.tr_name}"

    class Meta:
        db_table = 'transportation'


class Services(models.Model):
    """Модель для выбора дополнительных сервисов в закаyз"""
    ser_name = models.CharField(max_length=255)
    ser_price = models.FloatField()

    def __repr__(self):
        return f'{self.ser_name} , {self.ser_price}'

    def __str__(self):
        return f'{self.ser_name} - {self.ser_price}'

    class Meta:
        db_table = 'services'


class Auction(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return f'{self.name}'
    class Meta:
        db_table = 'auction'

