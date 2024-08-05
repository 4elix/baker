from django.contrib import admin
from django.utils.html import format_html

from .models import Categories, ProductGallery, Products



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_display_links = ['pk']
    search_fields = ['name']


class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'category', 'price', 'image']
    list_display_links = ['pk', 'title']
    list_editable = ['category']
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}
    inlines = [ProductGalleryInline]
    list_per_page = 3
    list_filter = ['category__name']

    field = ['__all__']

    @admin.action(description='Фотография')
    def image(self, obj):
        try:
            return format_html(f'<img src="{obj.get_first_image()}" width=80>')
        except:
            return '-'
