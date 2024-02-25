from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст")

    def __str__(self):
        return f"{self.title}"


class News(models.Model):
    news_title = models.CharField(max_length=50, verbose_name="Новость")
    news_content = models.TextField(verbose_name="Содержание новости")

    def __str__(self):
        return f"{self.news_title}"
