from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
import os

admin.site.register(LabIntroduction)
admin.site.register(LabProprietarySystem)
admin.site.register(Research)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pubdate', 'id')


admin.site.register(News, NewsAdmin)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('alt_name', 'thumbnail')
    readonly_fields = ('thumbnail',)

    def thumbnail(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % obj.img.url)

    thumbnail.short_description = 'thumbnail'


@admin.register(IndexImgCarousel)
class IndexImgCarouselAdmin(admin.ModelAdmin):
    list_display = ('alt_name', 'thumbnail', 'show_in_home')
    readonly_fields = ('thumbnail',)  # 必须加这行 否则访问编辑页面会报错

    def thumbnail(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % obj.img.url)

    thumbnail.short_description = 'thumbnail'

    def show_in_home(self, obj):
        return obj.show_in_home

    show_in_home.short_description = 'show in home'
