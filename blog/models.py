from django.db import models


class Blog(models.Model):
    title = models.CharField(verbose_name='Blog Title', max_length=100)
    date_created = models.DateTimeField(verbose_name='Date Created')
    description = models.TextField(verbose_name='Description')

