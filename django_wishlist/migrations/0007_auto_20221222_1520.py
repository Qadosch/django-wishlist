# Generated by Django 3.2.16 on 2022-12-22 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_wishlist', '0006_wish_visible'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gift',
            old_name='ammount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='wish',
            old_name='ammount',
            new_name='amount',
        ),
    ]