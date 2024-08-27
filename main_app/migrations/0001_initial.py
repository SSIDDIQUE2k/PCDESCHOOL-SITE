# Generated by Django 5.1 on 2024-08-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('grade', models.IntegerField()),
                ('description', models.TextField(max_length=250)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]
