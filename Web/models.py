from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

from mdeditor.fields import MDTextField


class Image(models.Model):
    img = models.ImageField(upload_to="Web/static/image")
    upload_time = models.DateTimeField("upload_time", auto_now_add=True)
    name = models.CharField(max_length=200)
    url = models.URLField("url(optional)", max_length=200, blank=True)


class IndexImgCarousel(Image):
    show_in_home = models.BooleanField(default=False)


@receiver(pre_delete, sender=Image)
def delete_image_file(sender, instance, **kwargs):
    file_path = instance.img.path
    if os.path.isfile(file_path):
        os.remove(file_path)


@receiver(pre_delete, sender=IndexImgCarousel)
def delete_image_file(sender, instance, **kwargs):
    file_path = instance.img.path
    if os.path.isfile(file_path):
        os.remove(file_path)


class LabIntroduction(models.Model):
    introduction = models.TextField()

    def __str__(self):
        return self.introduction


class LabProprietarySystem(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField("url(optional)", max_length=200, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = MDTextField()
    pubdate = models.DateTimeField("pubdate", auto_now_add=True)
    url = models.URLField(max_length=2000)


class News(Article):
    pass
