from django.contrib import admin
from .models import Blog, BlogComment, Category



class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_title', 'author', 'post_date', 'is_public')
    list_display_links = ('id','blog_title')
    search_fields = ('blog_title','author')
    list_per_page = 5
    list_editable = ('is_public',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment)
