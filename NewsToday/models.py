from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=255, unique=True)
    cat_description = RichTextField()

    def __str__(self):
        return self.cat_name