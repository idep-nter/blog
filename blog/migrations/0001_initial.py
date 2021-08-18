# Generated by Django 3.2.6 on 2021-08-17 09:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(null=True, upload_to='author')),
                ('about_me', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('excerpt', models.CharField(max_length=300)),
                ('image', models.ImageField(null=True, upload_to='posts')),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(50)])),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.author')),
                ('tags', models.ManyToManyField(to='blog.Tag')),
            ],
        ),
    ]
