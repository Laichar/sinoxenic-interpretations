from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    pages = models.IntegerField(default=0)
    native_language = models.CharField(max_length=3)
    pub_date = models.DateTimeField('date published')

class Category(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Item(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    zh = models.CharField(max_length=200)
    en = models.CharField(max_length=200)
    zh_trans = models.CharField(max_length=200)
    page = models.IntegerField(default=0)
