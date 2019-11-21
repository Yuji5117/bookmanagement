from django.db import models
from django.utils import timezone


class Category(models.Model):
    name_category = models.CharField(max_length=50)

    def __str__(self):
        return self.name_category


class Book(models.Model):
    auther = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, verbose_name='種類', on_delete=models.PROTECT)
    comment = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos', null=True)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
