# Generated by Django 4.0.6 on 2022-07-11 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Image', models.ImageField(height_field=100, upload_to='', width_field=100)),
                ('Description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=99)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
