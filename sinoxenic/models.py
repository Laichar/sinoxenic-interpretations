from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    pages = models.IntegerField(default=0)
    native_language = models.CharField(max_length=3)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.book_name

class Category(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.category_name

class Item(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    zh = models.CharField(max_length=200)
    en = models.CharField(max_length=200)
    zh_trans = models.CharField(max_length=200)
    page = models.IntegerField(default=0)
    def __str__(self):
        return self.text
