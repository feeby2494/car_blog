from django.db import models

from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Post(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='posts',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_desc = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

class Element(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='elements',
        on_delete=models.CASCADE
    )
    innerHtml = models.TextField(blank=True, null=True)
    element_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.element_type
