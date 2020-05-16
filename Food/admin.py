from django.contrib import admin
from .models import FoodBlogPost, FoodComment, FoodImage, FoodPost


class FoodPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on', 'published')
    search_fields = ['title', 'description']
    readonly_fields = ['images', 'sections']
    fields = ['cover_image', 'title', 'description', 'images', 'sections', 'published']


admin.site.register(FoodBlogPost, FoodPostAdmin)
admin.site.register(FoodComment)
admin.site.register(FoodImage)
admin.site.register(FoodPost)



