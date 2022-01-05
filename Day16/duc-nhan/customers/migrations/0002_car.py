# Generated by Django 4.0.1 on 2022-01-05 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
    ]