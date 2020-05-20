from django.contrib import admin

from .models import BlogPost, Comment, Image, Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on', 'published')
    search_fields = ['title', 'description']
    readonly_fields = ['images', 'sections']
    fields = ['cover_image', 'title', 'description', 'images', 'sections', 'published']


admin.site.register(BlogPost, PostAdmin)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Post)
admin.site.register(Category)
