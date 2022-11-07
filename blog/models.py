from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('view_post', kwargs={'post_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Category(models.Model):
    category = models.CharField(max_length=50, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('categoryPage', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'