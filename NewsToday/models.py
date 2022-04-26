from django.db import models
from ckeditor.fields import RichTextField
from datetime import date, datetime 

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=255, unique=True)
    cat_description = RichTextField()

    def __str__(self):
        return self.cat_name

class News(models.Model):
    news_id = models.BigAutoField(primary_key=True)
    cat_id = models.ForeignKey(Category, models.PROTECT)
    slug = models.CharField(max_length=255)
    news_title = models.CharField(max_length=255)
    news_content = models.TextField()
    news_image = models.ImageField(upload_to='news')
    date_posted = models.DateField(auto_now_add=False)
    date_updated = models.DateField(auto_now=False)
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()

    def __str__(self):
        return self.news_title

class Contact(models.Model):
    contact_id = models.BigAutoField(primary_key=True)
    contact_name = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.contact_email

class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    comment_content = models.TextField()
    news_id = models.ForeignKey(News, models.PROTECT)
    comment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment_content
