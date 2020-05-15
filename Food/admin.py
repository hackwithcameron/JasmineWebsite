from django.contrib import admin
from .models import FoodBlogPost, FoodComment, FoodImage


class FoodPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on', 'published')
    search_fields = ['title', 'description']
    readonly_fields = ['children_display']
    fields = ['cover_image', 'title', 'description', 'children_display', 'post', 'published']


admin.site.register(FoodBlogPost, FoodPostAdmin)
admin.site.register(FoodComment)
admin.site.register(FoodImage)



