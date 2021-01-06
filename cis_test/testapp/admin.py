from django.contrib import admin
from testapp.models import Categories, Product, Tag


class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ['name']


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['product_name', ]
    list_display = ['product_name', 'category']
    list_filter = ('category',)


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
