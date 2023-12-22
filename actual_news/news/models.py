from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(upload_to='users/',
                              null=True, blank=True,
                              verbose_name='Изображение')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категирия'
        verbose_name_plural = 'Категирии'


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(default='Здесь будет текст', verbose_name='Описание')
    # image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    image_src = models.CharField(max_length=255, verbose_name='Ссылка на изображение', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    text = models.TextField(verbose_name='Текст')
    profile_id = models.IntegerField(verbose_name='Id пользователя')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
