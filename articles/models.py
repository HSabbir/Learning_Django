from django.db import models
import datetime
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)