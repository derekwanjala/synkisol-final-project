# Generated by Django 4.0.4 on 2022-05-15 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_about_clients_strategy_team'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
                ('alt', models.CharField(max_length=60)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('alt', models.CharField(blank=True, max_length=60)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.service')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
    ]