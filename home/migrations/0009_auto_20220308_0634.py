# Generated by Django 2.2.12 on 2022-03-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_my_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_name',
            field=models.CharField(default=None, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='course',
            field=models.CharField(default=None, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='standard',
            field=models.CharField(default=None, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='writer',
            field=models.CharField(default=None, max_length=122, null=True),
        ),
    ]