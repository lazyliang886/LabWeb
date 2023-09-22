from django.contrib import admin
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

from mdeditor.fields import MDTextField


class Image(models.Model):
    img = models.ImageField(verbose_name="图片", upload_to="Web/image")
    upload_time = models.DateTimeField("upload_time", auto_now_add=True)
    alt_name = models.CharField(verbose_name="显示名称", max_length=200)
    url = models.URLField(verbose_name="链接（可不填）", max_length=200, blank=True)


class IndexImgCarousel(Image):
    show_in_home = models.BooleanField(verbose_name="是否展示在首页", default=False)

    class Meta:
        verbose_name_plural = "首页图像轮换"


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
    introduction = models.TextField(verbose_name="简介", blank=True)

    def __str__(self):
        return self.introduction

    class Meta:
        verbose_name_plural = "实验室介绍"


class LabLeadIn(models.Model):
    lead_in = models.TextField(blank=True)

    def __str__(self):
        return self.lead_in


class LabProprietarySystem(models.Model):
    name = models.CharField(verbose_name="名称", max_length=200)
    url = models.URLField("链接（可不填）", max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "实验室自研系统"


class Article(models.Model):
    title = models.CharField(verbose_name="标题", max_length=200)
    content = MDTextField(verbose_name="内容")
    pubdate = models.DateTimeField("发布日期", auto_now_add=True)


class News(Article):
    class Meta:
        verbose_name_plural = "新闻"


class Research(models.Model):
    content = MDTextField()

    class Meta:
        verbose_name_plural = "研究方向"


class Member(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=200)
    photo = models.ImageField(verbose_name="照片", upload_to="Web/image")


class Teacher(Member):
    title = models.CharField(verbose_name="职称", max_length=200)

    class Meta:
        verbose_name_plural = "教师信息"


class Postgraduate(Member):
    grade = models.CharField(verbose_name="年级", max_length=200)

    class Meta:
        verbose_name_plural = "研究生信息"


class Undergraduate(Member):
    grade = models.CharField(verbose_name="年级", max_length=200)

    class Meta:
        verbose_name_plural = "本科生信息"
