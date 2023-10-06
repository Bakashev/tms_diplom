from django.forms import ModelForm
from .models import Order, BalanceOperation, Correspondence
from users.models import User

class AllOrders(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(AllOrders, self).__init__(*args, **kwargs)
    class Meta:
        model = Order
        fields = ["id",
                  "name_auction",
                  "address_auction",
                  "number_order",
                  "model_transport",
                  "description",
                  "photo",
                  #"price",
                  "city_auction",
                  #"correspondence",
                  "place_delivery",
                  "transportation",
                  #"user",
                  "service",
                  ]

class UserOperationsBalance(ModelForm):
    """Форма для пополнения баланса пользователя"""
    def __init__(self, *args, **kwargs):
        super(UserOperationsBalance, self).__init__(*args, **kwargs)

    class Meta:
        model = BalanceOperation
        fields = ["sum"]


class UserCreateCorrespondence(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserCreateCorrespondence, self).__init__(*args, **kwargs)

    class Meta:
        model = Correspondence
        fields = ["message"]

