# Generated by Django 3.2.7 on 2021-12-06 18:27

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
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('mob_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=10000)),
                ('count', models.IntegerField(default=1)),
                ('image', models.ImageField(null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=120)),
                ('date_order', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('orderplaced', 'orderplaced'), ('dispatch', 'dispatch'), ('intransit', 'intransit'), ('delivered', 'delivered'), ('order_cancelled', 'order_cancelled')], default='orderplaced', max_length=120)),
                ('expected_delivery_date', models.DateField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.mobile')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('incart', 'incart'), ('cancelled', 'cancelled'), ('orderplaced', 'orderplaced')], default='incart', max_length=120)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.mobile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
