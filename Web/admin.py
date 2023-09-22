from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

admin.site.site_title = "智能计算与系统结构实验室"
admin.site.site_header = "智能计算与系统结构实验室"

admin.site.register(LabIntroduction)
admin.site.register(LabLeadIn)
admin.site.register(LabProprietarySystem)
admin.site.register(Research)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'thumbnail')

    def thumbnail(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % obj.photo.url)

    thumbnail.short_description = '照片'


admin.site.register(Teacher, TeacherAdmin)


class PostgraduateAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'thumbnail')

    def thumbnail(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % obj.photo.url)

    thumbnail.short_description = '照片'


admin.site.register(Postgraduate, PostgraduateAdmin)


class UndergraduateAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'thumbnail')

    def thumbnail(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % obj.photo.url)

    thumbnail.short_description = '照片'


admin.site.register(Undergraduate, UndergraduateAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pubdate', 'id')
    search_fields = ["title", "content"]


admin.site.register(News, NewsAdmin)


class IndexImgCarouselAdmin(admin.ModelAdmin):
    list_display = ('alt_name', 'thumbnail', 'show_in_home')

    def thumbnail(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % obj.img.url)

    thumbnail.short_description = '缩略图'

    def show_in_home(self, obj):
        return obj.show_in_home

    show_in_home.short_description = '是否展示在首页'


admin.site.register(IndexImgCarousel, IndexImgCarouselAdmin)
