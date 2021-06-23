from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import mark_safe
import datetime
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.text import slugify


# Create your models here.
class Category(MPTTModel):
    STATUS = (('True', 'Yes'), ('False', 'No'))
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS, null=True)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join(full_path[::-1])


# Create your models here.
class Brand(MPTTModel):
    STATUS = (('True', 'Yes'), ('False', 'No'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS, null=True)
    slug = models.SlugField(max_length=140, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']


# Create your models here.
class Product(models.Model):
    STATUS = (('True', 'Yes'), ('False', 'No'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_1 = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.BigIntegerField()
    min_amount = models.IntegerField()
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS, null=True)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image_1:
            return mark_safe('<img src="%s" style="width: 50px; height:50px;" />' % self.image_1.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
