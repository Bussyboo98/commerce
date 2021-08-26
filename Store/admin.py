from django.contrib import admin

from Store.models import *

admin.site.site_header = 'Django Ecommerce'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'author', 'slug', 'price', 'in_stock','is_active',
        'created', 'updated'
    ]
    list_filter = [
        'in_stock', 'is_active'
    ]
    prepopulated_fields = {'slug': ('title',)}
