from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from .models import Category, Product, Image, Brand


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['status']


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count', 'related_brands_count', 'related_brands_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Product,
                                                'category',
                                                'products_count',
                                                cumulative=False)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Brand,
            'category',
            'brands_cumulative_count',
            cumulative=True)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Brand,
            'category',
            'brands_count',
            cumulative=False)

        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'Related products (in tree)'

    def related_brands_count(self, instance):
        return instance.brands_count

    related_brands_count.short_description = 'Related brands (for this specific category)'

    def related_brands_cumulative_count(self, instance):
        return instance.brands_cumulative_count

    related_brands_cumulative_count.short_description = 'Related brands (in tree)'


class BrandAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Brand.objects.add_related_count(
            qs,
            Product,
            'brand',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Brand.objects.add_related_count(qs,
                                             Product,
                                             'brand',
                                             'products_count',
                                             cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = 'Related products (for this specific brand)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'Related products (in tree)'


class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['status']


class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'brand', 'status', 'image_tag']
    list_filter = ['category']
    list_filter_1 = ['brand']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Brand, BrandAdmin2)
