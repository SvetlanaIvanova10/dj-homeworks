# Generated by Django 2.2.10 on 2020-05-23 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200523_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theming',
            options={'verbose_name': 'Тема-статья', 'verbose_name_plural': 'Темы статей'},
        ),
    ]
