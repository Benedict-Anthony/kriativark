from django.contrib import admin

# Register your models here.

from .models import Tag, Post, Comments

class TagAdmin(admin.ModelAdmin):
    list_display = ("caption" ,"type",)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "excert", "date",)
    list_filter = ("date", "author", "tag",)
    prepopulated_fields = {"slug":("title",)}

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("name", "comment", "post",)

admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)



admin.site.site_header = "Kriativ Ark"