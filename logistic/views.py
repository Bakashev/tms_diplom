from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View, CreateView
from .forms import AllOrders, UserOperationsBalance, UserCreateCorrespondence
from .models import Order, Services, BalanceOperation, Correspondence
from django.urls import reverse_lazy, reverse
from users.models import User

class Home(View):

    def get(self, request):

        return render(self.request, 'home.html')

class ReestrOrders(View):
    def get(self, request):
        ords = Order.objects.all()
        return render(request, "orders.html", {'orders': ords})



class ShowOrder(DetailView):
    model = Order
    template_name = 'show_order.html'
    #ontext_object_name = 'orders'

class CreatOrder(CreateView):
    model = Order


    def get(self, request):
        return render(request, 'create_order.html', {'form': AllOrders})

    def post(self, request, *args, **kwargs):
        form = AllOrders(request.POST, request.FILES)
        print(request.POST.getlist('name_auction'))
        print(request.POST.getlist('address_auction'))
        print(request.POST.getlist('number_order'))
        print(request.POST.getlist('model_transport'))
        print(request.POST.getlist('description'))
        print(request.POST.getlist('photo'))
        print(request.POST.getlist('city_auction'))
        print('PD', end='')
        print(request.POST.getlist("place_delivery"))
        print(request.POST.getlist('transportation'))
        print(request.POST.getlist('service'))
        print(request.POST.getlist('correspondence'))
        print(request.POST.getlist('price'))
        print(request.user)
        print(request.POST.getlist('service'))
        if form.is_valid():
            name_auction = form.cleaned_data['name_auction']
            address_auction = form.cleaned_data['address_auction']
            number_order = form.cleaned_data['number_order']
            model_transport = form.cleaned_data['model_transport']
            description = form.cleaned_data['description']
            photo = form.cleaned_data['photo']
            city_auction = form.cleaned_data['city_auction']
            place_delivery = form.cleaned_data['place_delivery']
            transportation = form.cleaned_data['transportation']
            service = form.cleaned_data['service']
            print( 'Service', service)
            services = Services.objects.filter(order__service__in=service)
            print(services)


            correspondence = form.cleaned_data['correspondence']
            #price = form.cleaned_data['price']

            order = self.model.objects.create(
                name_auction=name_auction,
                address_auction=address_auction,
                number_order=number_order,
                model_transport=model_transport,
                description=description,
                photo=photo,

                city_auction=city_auction,
                place_delivery=place_delivery,
                transportation=transportation,
                #service=service,
                correspondence=correspondence,
                user=request.user

            )
            # Добавление серивсов в связанную таблицу через M2M
            order.service.set(service)
            order.save()
            print(order.service)
            order.price = order.calculated_price()
            order.save(update_fields=['price'])
            return redirect(reverse('show_order', kwargs={'pk': order.id}))

class ClientCard(DetailView):
    """Просмотр информации о клиенте (UserName, баланс)"""
    model = User
    template_name = 'client.html'


class CreateUserBalance(CreateView):
    model = BalanceOperation
    #fields = ['sum']

    def get(self, request, pk):
        return render(request, 'upload_balance.html', {'form': UserOperationsBalance})

    def post(self, request, *args, **kwargs):
         form = UserOperationsBalance(request.POST)

         if form.is_valid():
             sum = form.cleaned_data['sum']

             if sum > 0:
                balance_operation = self.model.objects.create(
                 sum=sum,
                 user=request.user
                )

                balance_operation.save()
                #balance_operation.user_balance()
                balance_operation.user.user_balance()

         return redirect(reverse('orders'))


class CreateCorrespondence(CreateView):
    model = Correspondence
    fields = ["message"]

    def get(self, request, pk):
        return render(request, 'create_correspondance.html', {'form': UserCreateCorrespondence})

    def post(self, request, pk):
        form = UserCreateCorrespondence(request.POST)
        if form.is_valid():
            message = request.POST.get('message')
        #order = get_object_or_404(Correspondence, id=pk)
        username = request.user.id
        Correspondence.objects.create(
            user_id=username,
            message=message,
            order_id_id=pk)

        return redirect(reverse('show_order', kwargs={'pk': pk}))

class ShowCorrespondence(ListView):
    model = Correspondence
    template_name = 'show_correspondance.html'
    context_object_name = 'correspondence'

    def get_queryset(self, request):
        return Correspondence.objects.select_related("order_id").filter(order_id=request)





