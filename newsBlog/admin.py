from django.contrib import admin
from .models import Tag, News, IP
admin.site.register(Tag)


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('header', )}


admin.site.register(News, NewsAdmin)
admin.site.register(IP)