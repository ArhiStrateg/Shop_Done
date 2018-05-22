from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Dolgnoct(models.Model):
    dolgnost_nasvanie = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return "%s" % self.dolgnost_nasvanie

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class User_Login(models.Model):
    login_login = models.CharField(max_length=64, blank=True, null=True)
    password_login = models.CharField(max_length=64, blank=True, null=True)
    is_active_login = models.BooleanField(default=True)
    session_key_login = models.CharField(max_length=124, blank=True, null=True, default=None)

    created_login = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_login = models.DateTimeField(auto_now_add=False, auto_now=True)

    name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    surname = models.CharField(max_length=64, blank=True, null=True)

    dolgnoct = models.ForeignKey(Dolgnoct, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Пользователь для теневой области'
        verbose_name_plural = 'Пользователи для теневой области'


class Zakaz(models.Model):
    text_for_zakaz_main = models.TextField(blank=True, null=True, default=None)
    text_for_zakaz_main_ukr = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    title = models.CharField(max_length=320, blank=True, null=True, default=None)
    title_ukr = models.CharField(max_length=320, blank=True, null=True, default=None)
    keyword = models.CharField(max_length=512, blank=True, null=True, default=None)
    keyword_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)
    description = models.CharField(max_length=512, blank=True, null=True, default=None)
    description_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Главная - заказы/оплата/доставка'
        verbose_name_plural = 'Главная - заказы/оплата/доставка'


class Footer(models.Model):
    text = models.TextField(blank=True, null=True, default=None)
    text_ukr = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Информация - футер'
        verbose_name_plural = 'Информация - футер'


class Company(models.Model):
    text_for_company = models.TextField(blank=True, null=True, default=None)
    text_for_company_ukr = models.TextField(blank=True, null=True, default=None)
    img_for_company = models.ImageField(upload_to='compamy_img/')
    is_active = models.BooleanField(default=True)

    title = models.CharField(max_length=320, blank=True, null=True, default=None)
    title_ukr = models.CharField(max_length=320, blank=True, null=True, default=None)
    keyword = models.CharField(max_length=512, blank=True, null=True, default=None)
    keyword_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)
    description = models.CharField(max_length=512, blank=True, null=True, default=None)
    description_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)


    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Информация - компания'
        verbose_name_plural = 'Информация - компания'


class Contscts(models.Model):
    text_for_contscts_main = models.TextField(blank=True, null=True, default=None)
    text_for_contscts_main_ukr = models.TextField(blank=True, null=True, default=None)
    text_for_contscts_pech = models.TextField(blank=True, null=True, default=None)
    text_for_contscts_pech_ukr = models.TextField(blank=True, null=True, default=None)
    text_for_contscts_auto = models.TextField(blank=True, null=True, default=None)
    text_for_contscts_auto_ukr = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    title = models.CharField(max_length=320, blank=True, null=True, default=None)
    title_ukr = models.CharField(max_length=320, blank=True, null=True, default=None)
    keyword = models.CharField(max_length=512, blank=True, null=True, default=None)
    keyword_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)
    description = models.CharField(max_length=512, blank=True, null=True, default=None)
    description_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)

    phone_1_for_contscts = models.CharField(max_length=64, blank=True, null=True, default=None)
    phone_1_for_contscts_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    text_phone_1_for_contscts = models.CharField(max_length=64, blank=True, null=True, default=None)
    text_phone_1_for_contscts_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    phone_2_for_contscts = models.CharField(max_length=64, blank=True, null=True, default=None)
    phone_2_for_contscts_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    text_phone_2_for_contscts = models.CharField(max_length=64, blank=True, null=True, default=None)
    text_phone_2_for_contscts_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    adress_adress_for_contscts = models.CharField(max_length=64, blank=True, null=True, default=None)
    adress_adress_for_contscts_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    adress_local_for_contscts = models.CharField(max_length=64, blank=True, null=True, default=None)
    adress_local_for_contscts_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    time_b_for_contscts = models.CharField(max_length=64, blank=True, null=True, default=None)
    time_b_for_contscts_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    time_v_for_contscts = models.CharField(max_length=64, blank=True, null=True, default=None)
    time_v_for_contscts_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    playment_for_contscts_text = models.TextField(blank=True, null=True, default=None)
    playment_for_contscts_text_ukr = models.TextField(blank=True, null=True, default=None)
    playment_for_contscts_img = models.ImageField(upload_to='contsct_img/')


    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Diler_Otdel(models.Model):
    text_diler_otdel = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    title = models.CharField(max_length=320, blank=True, null=True, default=None)
    keyword = models.CharField(max_length=512, blank=True, null=True, default=None)
    description = models.CharField(max_length=512, blank=True, null=True, default=None)

    phone_1_for_do = models.CharField(max_length=64, blank=True, null=True, default=None)
    text_phone_1_for_do = models.CharField(max_length=64, blank=True, null=True, default=None)
    phone_2_for_do = models.CharField(max_length=64, blank=True, null=True, default=None)
    text_phone_2_for_do = models.CharField(max_length=64, blank=True, null=True, default=None)
    phone_3_for_do = models.CharField(max_length=64, blank=True, null=True, default=None)
    text_phone_3_for_do = models.CharField(max_length=64, blank=True, null=True, default=None)

    time_work_b = models.CharField(max_length=64, blank=True, null=True, default=None)
    time_work_b_time = models.CharField(max_length=64, blank=True, null=True, default=None)
    time_work_s = models.CharField(max_length=64, blank=True, null=True, default=None)
    time_work_s_time = models.CharField(max_length=64, blank=True, null=True, default=None)
    time_work_v = models.CharField(max_length=64, blank=True, null=True, default=None)
    time_work_v_time = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Дилерский отдел'
        verbose_name_plural = 'Дилерский отдел'


class Diler_Otdel_Сonttacts(models.Model):
    connect = models.ForeignKey(Diler_Otdel, blank=True, null=True, default=None)
    fio = models.CharField(max_length=64, blank=True, null=True, default=None)
    dolgnost = models.CharField(max_length=64, blank=True, null=True, default=None)
    phone = models.CharField(max_length=64, blank=True, null=True, default=None)
    email = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Дилерский отдел - контакты'
        verbose_name_plural = 'Дилерский отдел - контакты'


class Projects_Materials(models.Model):
    text_for_project = models.TextField(blank=True, null=True, default=None)
    text_for_project_ukr = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    title = models.CharField(max_length=320, blank=True, null=True, default=None)
    title_ukr = models.CharField(max_length=320, blank=True, null=True, default=None)
    keyword = models.CharField(max_length=512, blank=True, null=True, default=None)
    keyword_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)
    description = models.CharField(max_length=512, blank=True, null=True, default=None)
    description_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)

    phone_1 = models.CharField(max_length=64, blank=True, null=True, default=None)
    phone_1_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    test_phone_1 = models.CharField(max_length=64, blank=True, null=True, default=None)
    test_phone_1_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    phone_2 = models.CharField(max_length=64, blank=True, null=True, default=None)
    phone_2_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    test_phone_2 = models.CharField(max_length=64, blank=True, null=True, default=None)
    test_phone_2_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    adress_adress = models.CharField(max_length=64, blank=True, null=True, default=None)
    adress_adress_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    adress_local = models.CharField(max_length=64, blank=True, null=True, default=None)
    adress_local_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    time_b = models.CharField(max_length=64, blank=True, null=True, default=None)
    time_b_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    time_v = models.CharField(max_length=64, blank=True, null=True, default=None)
    time_v_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)



    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Проектные материалы'
        verbose_name_plural = 'Проектные материалы'


class Search_Low_Addition(models.Model):
    session_key = models.CharField(max_length=124, blank=True, null=True, default=None)
    response = models.CharField(max_length=256, blank=True, null=True, default=None)

    request_get_nhs = models.CharField(max_length=124, null=True, default=None)
    request_get_manafacturer = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_size = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_country = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_price = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_availability = models.CharField(max_length=124, blank=True, null=True, default=None)

    request_get_texturer = models.CharField(max_length=612, blank=True, null=True, default=None)
    request_get_facturer = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_colour = models.CharField(max_length=612, blank=True, null=True, default=None)
    request_get_application = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_style = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_type_material = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_type_floor = models.CharField(max_length=124, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Поиск - сложный поиск'
        verbose_name_plural = 'Поиск - сложный поиск'


class Search_Diller_Otdel(models.Model):
    session_key = models.CharField(max_length=124, blank=True, null=True, default=None)
    response = models.CharField(max_length=256, blank=True, null=True, default=None)

    request_get_manafacturer = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_country = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_price = models.CharField(max_length=124, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Поиск - дилерский отдел'
        verbose_name_plural = 'Поиск - дилерский отдел'


class Search_Manafactory(models.Model):
    session_key = models.CharField(max_length=124, blank=True, null=True, default=None)
    response = models.CharField(max_length=256, blank=True, null=True, default=None)

    request_get_country = models.CharField(max_length=124, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Поиск - каталог'
        verbose_name_plural = 'Поиск - каталог'


class Search_Manafactory_Single(models.Model):
    session_key = models.CharField(max_length=124, blank=True, null=True, default=None)
    response = models.CharField(max_length=256, blank=True, null=True, default=None)

    request_get_price = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_availability = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_application = models.CharField(max_length=124, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Поиск - один производитель'
        verbose_name_plural = 'Поиск - один производитель'


class Search_For_Project(models.Model):
    session_key = models.CharField(max_length=124, blank=True, null=True, default=None)
    response = models.CharField(max_length=256, blank=True, null=True, default=None)

    request_get_manafacturer = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_country = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_price = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_availability = models.CharField(max_length=124, blank=True, null=True, default=None)

    request_get_application = models.CharField(max_length=124, blank=True, null=True, default=None)
    request_get_type_material = models.CharField(max_length=124, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Поиск - проекты'
        verbose_name_plural = 'Поиск - проекты'


class Search_Low(models.Model):
    search = models.ForeignKey(Search_Low_Addition, blank=True, null=True, default=None)
    search_text = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Search (Запрос по поиску)'
        verbose_name_plural = 'Search (Запрос по поиску)'


class Search_Search(models.Model):
    session_key = models.CharField(max_length=124, blank=True, null=True, default=None)
    response = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Поиск - по единичному слову'
        verbose_name_plural = 'Поиск - по единичному слову'


class For_Main(models.Model):
    text = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    title = models.CharField(max_length=320, blank=True, null=True, default=None)
    title_ukr = models.CharField(max_length=320, blank=True, null=True, default=None)
    keyword = models.CharField(max_length=512, blank=True, null=True, default=None)
    keyword_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)
    description = models.CharField(max_length=512, blank=True, null=True, default=None)
    description_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)


    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Для главной страницы'
        verbose_name_plural = 'Для главной страницы'


class For_IMG_Main(models.Model):
    text_for_main_img = models.CharField(max_length=64, blank=True, null=True, default=None)
    text_for_main_img_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)
    name_main = models.ForeignKey(For_Main, blank=True, null=True, default=None)
    image_main = models.ImageField(upload_to='main_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Катринки для слайдера на главной странице'
        verbose_name_plural = 'Катринки для слайдера на главной странице'


class For_Сatalog(models.Model):
    text = models.TextField(blank=True, null=True, default=None)
    text_ukr = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    image_catalog_main = models.ImageField(upload_to='image_catalog_main/', null=True, default=None)

    title = models.CharField(max_length=320, blank=True, null=True, default=None)
    title_ukr = models.CharField(max_length=320, blank=True, null=True, default=None)
    keyword = models.CharField(max_length=512, blank=True, null=True, default=None)
    keyword_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)
    description = models.CharField(max_length=512, blank=True, null=True, default=None)
    description_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'

