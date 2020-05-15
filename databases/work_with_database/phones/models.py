from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.ForeignKey
    name = models.CharField(max_length=64, verbose_name='Модель телефона')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='', verbose_name='Изображение')
    release_date = models.DateField()
    lte_exists = models.TextField()
    slug = models.SlugField(blank=True, unique=True, verbose_name='URL')

