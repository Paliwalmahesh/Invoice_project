# Generated by Django 3.1.2 on 2021-10-19 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_items_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='grand_total',
            field=models.FloatField(default=1),
        ),
    ]
