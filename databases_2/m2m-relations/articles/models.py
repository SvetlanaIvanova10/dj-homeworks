from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение' )
    # thems = models.ManyToManyField(Theme, through='Theming', through_fields=('article', 'theme'), )
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Theme(models.Model):
    name = models.CharField(max_length=256, verbose_name='Тема')
    thems = models.ManyToManyField(Article, through='Theming', through_fields=('theme', 'article'),)
    # thems = models.ManyToManyField(Article, verbose_name='Тема')
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name

class Theming(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name='Тема')
    main_theme = models.BooleanField(verbose_name='Основная тема')

    class Meta:
        verbose_name = 'Тема-статья'
        verbose_name_plural = 'Темы статей'

