from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'category',)
    list_display_links = ('id', 'title', 'created_at',)
    list_editable = ('category',)
    list_filter = ('category', )

admin.site.register(Article, ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_display_links = ('id',)
    search_fields = ('title',)

admin.site.register(Category, CategoryAdmin)