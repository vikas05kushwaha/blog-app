# Generated by Django 2.2.12 on 2022-02-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('description', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=122)),
                ('userid', models.CharField(max_length=122)),
            ],
        ),
    ]