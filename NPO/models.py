from django.db import models

from users.models import User


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')
    image = models.ImageField(null=True, blank=True)
    link = models.URLField(null=True)

    def short_text(self):
        return self.text[:20]

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    image = models.ImageField(null=True)
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True, related_name='images')

    def __str__(self):
        return self.image.url


class TypeLaw(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Law(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    law_type = models.ForeignKey(TypeLaw, on_delete=models.SET_NULL, null=True)


PUBLICATION_TYPES = (
    (1, 'Публикации ICNL'),
    (2, 'Другие публикации')
)


class Publication(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    file = models.FileField(null=True, blank=True)
    types = models.IntegerField(choices=PUBLICATION_TYPES, default=1)


class Question(models.Model):
    question_text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class FavouriteNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
