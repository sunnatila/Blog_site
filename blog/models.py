from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models

from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=300)
    summary = models.CharField(max_length=500)
    body = RichTextField()
    at_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=250)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    at_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.comment}"

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.article.pk)])
