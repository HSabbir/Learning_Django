from django.db import models
import datetime
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_save

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)

        super().save(*args, **kwargs)

def article_pre_save(sender,instance, *args, **kwargs):
    print('pre_save')
    print(sender,instance)
    if instance.slug is None:
        instance.slug = slugify(instance.title)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender,instance, created, *args, **kwargs):
    print('post_save')
    if created:
        instance.slug = slugify(instance.title)
        instance.save()


post_save.connect(article_post_save, sender=Article)