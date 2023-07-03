from django.contrib import admin
from .models import Product, Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price',  'image']
    list_filter = ['name']
    search_fields = ['name']
    list_editable = ['price']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_header = "E-Commerce Admin"
admin.site.site_title = "E-Commerce Admin Portal"
admin.site.index_title = "Welcome to E-Commerce Portal"