# Generated by Django 2.2.10 on 2020-05-23 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme',
            options={'verbose_name': 'Тема', 'verbose_name_plural': 'Темы'},
        ),
    ]
