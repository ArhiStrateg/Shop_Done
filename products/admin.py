from django.contrib import admin
from products.models import Manufacturer, Price_Group, Availability, Collection, Collection_Image, Size, Product_Type, \
    Product, Product_Image, Manufacturer_Country, Manufacturer_Image, Collection_Search_NHS, Collection_Application_For_Search, \
    Collection_Type_Material_For_Search, Collection_Texturer_For_Search, Collection_Facturer_For_Search, Collection_Style_For_Search, \
    Collection_Floor_For_Search, Collection_Colour_For_Search

from redactor.widgets import RedactorEditor
from django import forms

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget

# Register your models here.

class Manufacturer_Inlines(admin.TabularInline):
    model = Manufacturer
    extra = 0


class Manufacturer_Image_Inlines(admin.TabularInline):
    model = Manufacturer_Image
    extra = 0


class Collection_Inlines(admin.TabularInline):
    model = Collection
    extra = 0


class Collection_Application_For_Search_Inlines(admin.TabularInline):
    model = Collection_Application_For_Search
    extra = 0


class Collection_Type_Material_For_Search_Inlines(admin.TabularInline):
    model = Collection_Type_Material_For_Search
    extra = 0


class Collection_Texturer_For_Search_Inlines(admin.TabularInline):
    model = Collection_Texturer_For_Search
    extra = 0


class Collection_Facturer_For_Search_Inlines(admin.TabularInline):
    model = Collection_Facturer_For_Search
    extra = 0


class Collection_Style_For_Search_Inlines(admin.TabularInline):
    model = Collection_Style_For_Search
    extra = 0


class Collection_Floor_For_Search_Inlines(admin.TabularInline):
    model = Collection_Floor_For_Search
    extra = 0


class Collection_Colour_For_Search_Inlines(admin.TabularInline):
    model = Collection_Colour_For_Search
    extra = 0


class Collection_Image_Inlines(admin.TabularInline):
    model = Collection_Image
    extra = 0


class Product_Inlines(admin.TabularInline):
    model = Product
    extra = 0


class Product_Image_Inlines(admin.TabularInline):
    model = Product_Image
    extra = 0


class Manufacturer_Country_ImportExport(resources.ModelResource):

    class Meta:
        model = Manufacturer_Country


class Manufacturer_Country_Admin(ImportExportActionModelAdmin):
    resource_class = Manufacturer_Country_ImportExport
    list_display = [field.name for field in Manufacturer_Country._meta.fields if field.name != "id"]
    inlines = [Manufacturer_Inlines]

admin.site.register(Manufacturer_Country, Manufacturer_Country_Admin)


# class Manufacturer_Country_Admin(admin.ModelAdmin):
#     list_display = [field.name for field in Manufacturer_Country._meta.fields]
#     inlines = [Manufacturer_Inlines]
#
#     class Meta:
#         model = Manufacturer_Country
#
# admin.site.register(Manufacturer_Country, Manufacturer_Country_Admin)


class Manufacturer_Admin(forms.ModelForm):

    class Meta:
        model = Manufacturer
        widgets = {
           'description_manufacturer': RedactorEditor(),
           'description_manufacturer_ukr': RedactorEditor(),
           'short_description_manufacturer': RedactorEditor(),
           'short_description_manufacturer_ukr': RedactorEditor(),
        }
        fields = ("name_manufacturer", "manufacturer_country", "is_active", 'short_description_manufacturer', 'short_description_manufacturer_ukr',
                  'description_manufacturer', 'description_manufacturer_ukr', 'title', 'keyword', 'description', "image_logo_manufacturer")

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Manufacturer._meta.fields]
    inlines = [Collection_Inlines, Manufacturer_Image_Inlines]
    form = Manufacturer_Admin

admin.site.register(Manufacturer, ManufacturerAdmin)


class Manufacturer_Image_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Manufacturer_Image._meta.fields]
    inlines = []

    class Meta:
        model = Manufacturer_Image

admin.site.register(Manufacturer_Image, Manufacturer_Image_Admin)


class Price_Group_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Price_Group._meta.fields]
    inlines = [Collection_Inlines]

    class Meta:
        model = Price_Group

admin.site.register(Price_Group, Price_Group_Admin)


class Availability_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Availability._meta.fields]
    inlines = [Collection_Inlines]

    class Meta:
        model = Availability

admin.site.register(Availability, Availability_Admin)


class Collection_Search_NHS_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Collection_Search_NHS._meta.fields]
    inlines = [Collection_Inlines]

    class Meta:
        model = Collection_Search_NHS

admin.site.register(Collection_Search_NHS, Collection_Search_NHS_Admin)


class Collection_Admin(forms.ModelForm):

    class Meta:
        model = Collection
        widgets = {
           'description_collection': RedactorEditor(),
           'short_description_collection': RedactorEditor(),
           'description_collection_ukr': RedactorEditor(),
           'short_description_collection_ukr': RedactorEditor(),
        }
        fields = ("id_patch", "name_collection", "description_collection", "short_description_collection", "description_collection_ukr",
                  "short_description_collection_ukr", 'manufacturer_collection',
                  'availability_collection', 'price_group_collection', 'name_collection_nhs', 'is_active_collection', 'is_view_main',
                  'title', 'title_ukr', 'keyword', 'keyword_ukr', 'description', 'description_ukr', 'price_download',
                  'description_collection_mini', 'description_collection_mini_ukr', 'image_collection_mini')


class CollectionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Collection._meta.fields]
    inlines = [Collection_Application_For_Search_Inlines, Collection_Type_Material_For_Search_Inlines,
               Collection_Texturer_For_Search_Inlines, Collection_Facturer_For_Search_Inlines, Collection_Style_For_Search_Inlines,
               Collection_Floor_For_Search_Inlines, Collection_Colour_For_Search_Inlines, Collection_Image_Inlines, Product_Inlines]
    form = Collection_Admin

admin.site.register(Collection, CollectionAdmin)


class Collection_Application_For_Search_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Collection_Application_For_Search._meta.fields]
    inlines = []

    class Meta:
        model = Collection_Application_For_Search

admin.site.register(Collection_Application_For_Search, Collection_Application_For_Search_Admin)


class Collection_Type_Material_For_Search_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Collection_Type_Material_For_Search._meta.fields]
    inlines = []

    class Meta:
        model = Collection_Type_Material_For_Search

admin.site.register(Collection_Type_Material_For_Search, Collection_Type_Material_For_Search_Admin)


class Collection_Texturer_For_Search_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Collection_Texturer_For_Search._meta.fields]
    inlines = []

    class Meta:
        model = Collection_Texturer_For_Search

admin.site.register(Collection_Texturer_For_Search, Collection_Texturer_For_Search_Admin)


class Collection_Facturer_For_Search_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Collection_Facturer_For_Search._meta.fields]
    inlines = []

    class Meta:
        model = Collection_Facturer_For_Search

admin.site.register(Collection_Facturer_For_Search, Collection_Facturer_For_Search_Admin)


class Collection_Style_For_Search_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Collection_Style_For_Search._meta.fields]
    inlines = []

    class Meta:
        model = Collection_Style_For_Search

admin.site.register(Collection_Style_For_Search, Collection_Style_For_Search_Admin)


class Collection_Floor_For_Search_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Collection_Floor_For_Search._meta.fields]
    inlines = []

    class Meta:
        model = Collection_Floor_For_Search

admin.site.register(Collection_Floor_For_Search, Collection_Floor_For_Search_Admin)


class Collection_Colour_For_Search_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Collection_Colour_For_Search._meta.fields]
    inlines = []

    class Meta:
        model = Collection_Colour_For_Search

admin.site.register(Collection_Colour_For_Search, Collection_Colour_For_Search_Admin)


class Collection_Image_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Collection_Image._meta.fields]
    inlines = []

    class Meta:
        model = Collection_Image

admin.site.register(Collection_Image, Collection_Image_Admin)


class Size_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Size._meta.fields]
    inlines = [Product_Inlines]

    class Meta:
        model = Size

admin.site.register(Size, Size_Admin)


class Product_Type_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Product_Type._meta.fields]
    inlines = [Product_Inlines]

    class Meta:
        model = Product_Type

admin.site.register(Product_Type, Product_Type_Admin)


class Product_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [Product_Image_Inlines]

    class Meta:
        model = Product

admin.site.register(Product, Product_Admin)



class Product_Image_ImportExport(resources.ModelResource):

    class Meta:
        model = Product_Image


class Product_Image_Admin(ImportExportActionModelAdmin):
    resource_class = Product_Image_ImportExport
    list_display = [field.name for field in Product_Image._meta.fields if field.name != "id"]

admin.site.register(Product_Image, Product_Image_Admin)


# class Product_Image_Admin(admin.ModelAdmin):
#     list_display = [field.name for field in Product_Image._meta.fields]
#     inlines = []
#
#     class Meta:
#         model = Product_Image
#
# admin.site.register(Product_Image, Product_Image_Admin)




