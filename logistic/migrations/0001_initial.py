# Generated by Django 4.2.4 on 2023-08-29 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CityAuction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Correspondence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PlaceDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pd_name', models.CharField(max_length=250)),
                ('pd_address', models.CharField(max_length=250)),
                ('pd_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ser_name', models.CharField(max_length=250)),
                ('ser_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tr_name', models.CharField(max_length=250)),
                ('type_transport', models.CharField(max_length=250)),
                ('tr_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_auction', models.CharField(max_length=250)),
                ('address_auction', models.CharField(max_length=250)),
                ('number_order', models.IntegerField()),
                ('model_transport', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('photo', models.ImageField(default=None, null=True, upload_to='image')),
                ('price', models.FloatField()),
                ('city_auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='logistic.cityauction')),
                ('correspondence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correspond', to='logistic.correspondence')),
                ('place_delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery', to='logistic.placedelivery')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_service', to='logistic.services')),
                ('transportation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transport', to='logistic.transportation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='correspondence',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_core', to='logistic.order'),
        ),
        migrations.AddField(
            model_name='correspondence',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correspond', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BalanceOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.FloatField()),
                ('date_operation', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
