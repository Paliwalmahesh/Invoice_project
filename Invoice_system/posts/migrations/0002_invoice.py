# Generated by Django 3.1.2 on 2021-10-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invoice_Id', models.TextField(max_length=10)),
                ('total_cost', models.FloatField()),
            ],
        ),
    ]