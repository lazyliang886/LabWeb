from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
import os

admin.site.register(LabIntroduction)
admin.site.register(LabProprietarySystem)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pubdate', 'id')


admin.site.register(News, NewsAdmin)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail', 'file_name')
    readonly_fields = ('thumbnail',)

    def thumbnail(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % obj.img.url)

    thumbnail.short_description = 'thumbnail'

    def file_name(self, obj):
        return os.path.basename(obj.img.path)

    file_name.short_description = 'file name'


@admin.register(IndexImgCarousel)
class IndexImgCarouselAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail', 'show_in_home', 'file_name')
    readonly_fields = ('thumbnail',)  # 必须加这行 否则访问编辑页面会报错

    def thumbnail(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % obj.img.url)

    thumbnail.short_description = 'thumbnail'

    def show_in_home(self, obj):
        return obj.show_in_home

    show_in_home.short_description = 'show in home'

    def file_name(self, obj):
        return os.path.basename(obj.img.path)

    file_name.short_description = 'file name'
