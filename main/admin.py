from django.contrib import admin
from main.models import Search_Low, Search_Low_Addition, For_Сatalog, For_Main, For_IMG_Main, Projects_Materials, Contscts, \
    Search_For_Project, Diler_Otdel, Diler_Otdel_Сonttacts, Search_Diller_Otdel, Company, Footer, Search_Manafactory, \
    Search_Manafactory_Single, Search_Search, Zakaz, User_Login, Dolgnoct

from redactor.widgets import RedactorEditor
from django import forms


class Search_Low_Inlines(admin.TabularInline):
    model = Search_Low
    extra = 0


class For_IMG_Main_Inlines(admin.TabularInline):
    model = For_IMG_Main
    extra = 0


class Diler_Otdel_Сonttacts_Inlines(admin.TabularInline):
    model = Diler_Otdel_Сonttacts
    extra = 0

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class User_Login_Inlines(admin.TabularInline):
    model = User_Login
    extra = 0

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class User_Login_Admin(admin.ModelAdmin):
    list_display = [field.name for field in User_Login._meta.fields]
    inlines = []

    class Meta:
        model = Footer

admin.site.register(User_Login, User_Login_Admin)


class Dolgnoct_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Dolgnoct._meta.fields]
    inlines = [User_Login_Inlines]

    class Meta:
        model = Dolgnoct

admin.site.register(Dolgnoct, Dolgnoct_Admin)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class Diler_Otdel_Сonttacts_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Diler_Otdel_Сonttacts._meta.fields]
    inlines = []

    class Meta:
        model = Diler_Otdel_Сonttacts

admin.site.register(Diler_Otdel_Сonttacts, Diler_Otdel_Сonttacts_Admin)


class FooterAdmin(forms.ModelForm):
    class Meta:
        model = Footer
        widgets = {
            'text': RedactorEditor(),
            'text_ukr': RedactorEditor(),
        }
        fields = ("text", 'text_ukr', "is_active")


class Footer_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Footer._meta.fields]
    inlines = []
    form = FooterAdmin

    class Meta:
        model = Footer

admin.site.register(Footer, Footer_Admin)


class DilerOtdelAdmin(forms.ModelForm):
    class Meta:
        model = Diler_Otdel
        widgets = {
            'text_diler_otdel': RedactorEditor(),
        }
        fields = ("text_diler_otdel", "is_active", "phone_1_for_do", "text_phone_1_for_do", "phone_2_for_do", "text_phone_2_for_do",
                  "phone_3_for_do", "text_phone_3_for_do", "time_work_b", "time_work_b_time", "time_work_s", "time_work_s_time",
                  "time_work_v", "time_work_v_time", "title", "keyword", "description")


class Diler_Otdel_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Diler_Otdel._meta.fields]
    inlines = [Diler_Otdel_Сonttacts_Inlines]
    form = DilerOtdelAdmin

    class Meta:
        model = Diler_Otdel

admin.site.register(Diler_Otdel, Diler_Otdel_Admin)


class CompanyAdmin(forms.ModelForm):
    class Meta:
        model = Company
        widgets = {
            'text_for_company': RedactorEditor(),
            'text_for_company_ukr': RedactorEditor(),
        }
        fields = ("text_for_company", "text_for_company_ukr", "img_for_company", "is_active", "title", "title_ukr",
                  "keyword", "keyword_ukr", "description", "description_ukr")


class Company_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]
    inlines = []
    form = CompanyAdmin

    class Meta:
        model = Company

admin.site.register(Company, Company_Admin)


class ZakazAdmin(forms.ModelForm):
    class Meta:
        model = Zakaz
        widgets = {
            'text_for_zakaz_main': RedactorEditor(),
            'text_for_zakaz_main_ukr': RedactorEditor(),
        }
        fields = ("text_for_zakaz_main", "text_for_zakaz_main_ukr", "is_active", "title", "title_ukr", "keyword", "keyword_ukr",
                  "description", "description_ukr")


class Zakaz_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Zakaz._meta.fields]
    inlines = []
    form = ZakazAdmin

    class Meta:
        model = Zakaz

admin.site.register(Zakaz, Zakaz_Admin)


class ContactsAdmin(forms.ModelForm):
    class Meta:
        model = Contscts
        widgets = {
            'text_for_contscts_main': RedactorEditor(),
            'text_for_contscts_main_ukr': RedactorEditor(),
            'text_for_contscts_pech': RedactorEditor(),
            'text_for_contscts_pech_ukr': RedactorEditor(),
            'text_for_contscts_auto': RedactorEditor(),
            'text_for_contscts_auto_ukr': RedactorEditor(),
            'playment_for_contscts_text': RedactorEditor(),
            'playment_for_contscts_text_ukr': RedactorEditor(),
        }
        fields = ("text_for_contscts_main", "text_for_contscts_main_ukr",
                  "text_for_contscts_pech", "text_for_contscts_pech_ukr",
                  "text_for_contscts_auto", "text_for_contscts_auto_ukr",
                  "is_active", "phone_1_for_contscts", "phone_1_for_contscts_ukr",
                  "text_phone_1_for_contscts", "text_phone_1_for_contscts_ukr",
                  "phone_2_for_contscts", "phone_2_for_contscts_ukr",
                  "text_phone_2_for_contscts", "text_phone_2_for_contscts_ukr",
                  "adress_adress_for_contscts", "adress_adress_for_contscts_ukr",
                  "adress_local_for_contscts", "adress_local_for_contscts_ukr",
                  "time_b_for_contscts", "time_b_for_contscts_ukr",
                  "time_v_for_contscts", "time_v_for_contscts_ukr",
                  "playment_for_contscts_text", "playment_for_contscts_text_ukr",
                  "playment_for_contscts_img",
                  "title", "title_ukr", "keyword", "keyword_ukr", "description", "description_ukr")


class Contacts_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Contscts._meta.fields]
    inlines = []
    form = ContactsAdmin

    class Meta:
        model = Contscts

admin.site.register(Contscts, Contacts_Admin)


class ProjectsMaterialsAdmin(forms.ModelForm):
    class Meta:
        model = Projects_Materials
        widgets = {
            'text_for_project': RedactorEditor(),
            'text_for_project_ukr': RedactorEditor(),
        }
        fields = ("text_for_project", "text_for_project_ukr", "is_active", "phone_1", "phone_1_ukr", "test_phone_1", "test_phone_1_ukr",
                  "phone_2", "phone_2_ukr", "test_phone_2", "test_phone_2_ukr", "adress_adress", "adress_adress_ukr",
                  "adress_local", "adress_local_ukr", "time_b", "time_b_ukr", "time_v", "time_v_ukr", "title", "title_ukr",
                  "keyword", "keyword_ukr", "description", "description_ukr")


class Projects_Materials_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Projects_Materials._meta.fields]
    inlines = []
    form = ProjectsMaterialsAdmin

    class Meta:
        model = Projects_Materials


admin.site.register(Projects_Materials, Projects_Materials_Admin)


class For_IMG_Main_Admin(admin.ModelAdmin):
    list_display = [field.name for field in For_IMG_Main._meta.fields]
    inlines = []

    class Meta:
        model = For_IMG_Main

admin.site.register(For_IMG_Main, For_IMG_Main_Admin)


class Search_Low_Addition_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Search_Low_Addition._meta.fields]
    inlines = [Search_Low_Inlines]

    class Meta:
        model = Search_Low_Addition

admin.site.register(Search_Low_Addition, Search_Low_Addition_Admin)


class Search_For_Project_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Search_For_Project._meta.fields]

    class Meta:
        model = Search_For_Project

admin.site.register(Search_For_Project, Search_For_Project_Admin)


class Search_Manafactory_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Search_Manafactory._meta.fields]

    class Meta:
        model = Search_Manafactory

admin.site.register(Search_Manafactory, Search_Manafactory_Admin)


class Search_Manafactory_Single_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Search_Manafactory_Single._meta.fields]

    class Meta:
        model = Search_Manafactory_Single

admin.site.register(Search_Manafactory_Single, Search_Manafactory_Single_Admin)


class Search_Diller_Otdel_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Search_Diller_Otdel._meta.fields]

    class Meta:
        model = Search_Diller_Otdel

admin.site.register(Search_Diller_Otdel, Search_Diller_Otdel_Admin)


class Search_Low_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Search_Low._meta.fields]
    inlines = []

    class Meta:
        model = Search_Low

admin.site.register(Search_Low, Search_Low_Admin)


class Search_Search_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Search_Search._meta.fields]
    inlines = []

    class Meta:
        model = Search_Search

admin.site.register(Search_Search, Search_Search_Admin)


class ForСatalogAdmin(forms.ModelForm):

    class Meta:
        model = For_Сatalog
        widgets = {
           'text': RedactorEditor(),
           'text_ukr': RedactorEditor(),
        }
        fields = ("text", "text_ukr", "is_active", "image_catalog_main", "title", "title_ukr", "keyword", "keyword_ukr", "description", "description_ukr")

class For_Сatalog_Admin(admin.ModelAdmin):
    list_display = [field.name for field in For_Сatalog._meta.fields]
    inlines = []
    form = ForСatalogAdmin


    class Meta:
        model = For_Сatalog

admin.site.register(For_Сatalog, For_Сatalog_Admin)


class For_Main_Admin(admin.ModelAdmin):
    list_display = [field.name for field in For_Main._meta.fields]
    inlines = [For_IMG_Main_Inlines]

    class Meta:
        model = For_Main

admin.site.register(For_Main, For_Main_Admin)


