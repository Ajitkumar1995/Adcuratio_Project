# Generated by Django 3.1 on 2020-08-09 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=64)),
                ('buyer', models.CharField(max_length=64)),
                ('invoice_no', models.CharField(max_length=64)),
                ('date', models.CharField(max_length=64)),
            ],
        ),
    ]
