# Generated by Django 2.2.12 on 2022-03-09 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_my'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jeans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
    ]