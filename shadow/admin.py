from django.contrib import admin
from shadow.models import Statistic_Find_Simple, Statistic_User_Sing_In_ColProd, Statistic_Find_Bloc, Log_In_Site, Eye


class Eye_Inlines(admin.TabularInline):
    model = Eye
    extra = 0


class Statistic_Find_Bloc_Admin (admin.ModelAdmin):
    list_display = [field.name for field in Statistic_Find_Bloc._meta.fields]

    class Meta:
        model = Statistic_Find_Bloc

admin.site.register(Statistic_Find_Bloc, Statistic_Find_Bloc_Admin)


class Statistic_Find_Simple_Admin (admin.ModelAdmin):
    list_display = [field.name for field in Statistic_Find_Simple._meta.fields]

    class Meta:
        model = Statistic_Find_Simple

admin.site.register(Statistic_Find_Simple, Statistic_Find_Simple_Admin)


class Statistic_User_Sing_In_ColProd_Admin (admin.ModelAdmin):
    list_display = [field.name for field in Statistic_User_Sing_In_ColProd._meta.fields]

    class Meta:
        model = Statistic_User_Sing_In_ColProd

admin.site.register(Statistic_User_Sing_In_ColProd, Statistic_User_Sing_In_ColProd_Admin)


class Eye_Admin (admin.ModelAdmin):
    list_display = [field.name for field in Eye._meta.fields]

    class Meta:
        model = Eye

admin.site.register(Eye, Eye_Admin)


class Log_In_Site_Admin (admin.ModelAdmin):
    list_display = [field.name for field in Log_In_Site._meta.fields]
    inlines = [Eye_Inlines]

    class Meta:
        model = Log_In_Site

admin.site.register(Log_In_Site, Log_In_Site_Admin)
