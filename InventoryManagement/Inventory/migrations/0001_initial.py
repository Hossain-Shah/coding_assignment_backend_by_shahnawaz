# Generated by Django 4.0.1 on 2022-06-17 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('note', models.TextField()),
                ('stock', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.supplier')),
            ],
        ),
    ]