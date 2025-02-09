# Generated by Django 5.0.12 on 2025-02-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
    ]
