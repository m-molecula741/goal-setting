from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
# Create your models here.

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Book(models.Model):
    title = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    autor = models.CharField(max_length =150 , db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='books')
    date_pub = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=500, blank=True)

    def get_absolute_url(self):
        return reverse('book_detail_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('book_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['date_pub']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


