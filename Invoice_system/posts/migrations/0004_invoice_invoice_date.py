# Generated by Django 3.1.2 on 2021-10-13 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='Invoice_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
