from django.contrib import admin

from .models import Category, Color, Size, Marca, Product, ProductAttribute, Banner

admin.site.register(Size)
admin.site.register(Marca)
admin.site.register(Banner)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag_path')


admin.site.register(Category, CategoryAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'color_tag_path')


admin.site.register(Color, ColorAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'marca', 'color', 'size', 'status')
    list_editable = ('status',)


admin.site.register(Product, ProductAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'color', 'size')


admin.site.register(ProductAttribute, ProductAttributeAdmin)
