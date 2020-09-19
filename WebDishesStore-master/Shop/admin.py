from django.contrib import admin
from django.utils.translation import ugettext_lazy
from Shop.models import *
# Panel setup
# admin.AdminSite.site_title = ugettext_lazy("Shop")
# admin.AdminSite.site_header = ugettext_lazy('Shop admin panel')
# admin.AdminSite.index_title = ugettext_lazy('Admin panel')


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0
    fields = ['img', 'image_tag']
    readonly_fields = ['image_tag']
    # classes = ('grp-collapse grp-open',)
    # inline_classes = ('grp-collapse grp-open',)


class TagInline(admin.TabularInline):
    model = Tag
    extra = 0


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 0


class SaleInline(admin.TabularInline):
    model = Sale
    extra = 0


@admin.register(Product)
class AdminProd(admin.ModelAdmin):
    # model = Product
    class Meta:
        model = Product
        fields = '__all__'
    list_display = ('name', 'desc')
    list_filter = ('tag', 'subCategory')
    inlines = (PhotoInline, SaleInline, CategoryInline)
    # filter_horizontal = ['tag', 'subCategory']
    search_fields = ('name',)


# admin.site.register(Product, AdminProd)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(SubCategory)
