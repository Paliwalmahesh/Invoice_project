# Generated by Django 3.1.2 on 2021-10-13 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_invoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cost', models.FloatField()),
                ('description', models.TextField()),
                ('Invoice_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Invoice_no', to='posts.invoice')),
            ],
        ),
    ]
