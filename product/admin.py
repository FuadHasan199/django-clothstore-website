from django.contrib import admin
from . models import Category,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ['category_name','slug']

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ['category','product_name','price','stock','is_available']

admin.site.register(Product, ProductAdmin)