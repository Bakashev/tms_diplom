from django.contrib import admin
from logistic.models import Order, PlaceDelivery, Transportation, CityAuction, Services, Auction, Correspondence,\
    BalanceOperation

from users.models import User

admin.site.register(Order)
admin.site.register(User)
admin.site.register(PlaceDelivery)
admin.site.register(Transportation)
admin.site.register(CityAuction)
admin.site.register(Services)
admin.site.register(Auction)
admin.site.register(Correspondence)
admin.site.register(BalanceOperation)

