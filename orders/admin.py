from django.contrib import admin
from orders.models import ProductInOrder, Order, ProductInBasket, Status, Find_Project, Call_Me
from shadow.models import Send_Orders, Send_Project


class Send_Orders_Inline(admin.TabularInline):
    model = Send_Orders
    extra = 0


class Send_Project_Inline(admin.TabularInline):
    model = Send_Project
    extra = 0


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class StatusInline(admin.TabularInline):
    model = Status
    extra = 0


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0


class StatusAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]
    inlines = [OrderInline]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)


class OrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline, Send_Orders_Inline]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)


class ProductInBasketAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)


class Find_ProjectAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Find_Project._meta.fields]
    inlines = [Send_Project_Inline]

    class Meta:
        model = Find_Project

admin.site.register(Find_Project, Find_ProjectAdmin)


class Send_Orders_Admin (admin.ModelAdmin):
    list_display = [field.name for field in Send_Orders._meta.fields]

    class Meta:
        model = Send_Orders

admin.site.register(Send_Orders, Send_Orders_Admin)


class Send_Project_Admin (admin.ModelAdmin):
    list_display = [field.name for field in Send_Project._meta.fields]

    class Meta:
        model = Send_Project

admin.site.register(Send_Project, Send_Project_Admin)


class Call_Me_Admin (admin.ModelAdmin):
    list_display = [field.name for field in Call_Me._meta.fields]

    class Meta:
        model = Call_Me

admin.site.register(Call_Me, Call_Me_Admin)