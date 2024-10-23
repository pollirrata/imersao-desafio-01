from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Nome")
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="Título")
    content = models.TextField(verbose_name="Texto")
    created_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', verbose_name="Tags")

    def __str__(self):
        return self.title




