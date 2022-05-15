# Generated by Django 4.0.4 on 2022-05-15 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('alt', models.CharField(blank=True, max_length=60)),
                ('icon', models.CharField(max_length=20)),
                ('detail', models.CharField(max_length=255)),
                ('short_detail', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('portfolio_title', models.CharField(max_length=50)),
                ('portfolio_image', models.ImageField(upload_to='images/')),
                ('portfolio_alt', models.CharField(blank=True, max_length=60)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'services',
            },
        ),
    ]