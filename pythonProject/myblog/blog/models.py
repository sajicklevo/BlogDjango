from django.db import models


class Post(models.Model):
    title = models.CharField('Название',max_length=100)
    content = models.CharField('Анонс',max_length=250)
    text = models.TextField('Статья')
    published_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title




