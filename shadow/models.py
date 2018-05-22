from django.db import models
from orders.models import Find_Project, Order
from main.models import User_Login



class Send_Orders(models.Model):
    text_send = models.TextField(blank=True, null=True, default=None)
    order_img = models.FileField(upload_to='shadow_orders/')
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    autor = models.ForeignKey(User_Login, blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Сообщения - ордер'
        verbose_name_plural = 'Сообщения - ордер'


class Send_Project(models.Model):
    text_send = models.TextField(blank=True, null=True, default=None)
    project_img = models.FileField(upload_to='shadow_projects/')
    project = models.ForeignKey(Find_Project, null=True, default=None)
    autor = models.ForeignKey(User_Login, blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Сообщения - проект'
        verbose_name_plural = 'Сообщения - проект'


class Statistic_Find_Simple(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    session_key = models.CharField(max_length=64, blank=True, null=True, default=None)
    find_collections = models.TextField(blank=True, null=True, default=None)
    find_manafacturer = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Статистика простого поиска'
        verbose_name_plural = 'Статистика простого поиска'


class Statistic_User_Sing_In_ColProd(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    session_key = models.CharField(max_length=64, blank=True, null=True, default=None)
    collection = models.TextField(blank=True, null=True, default=None)
    collection_product = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Статистика перехода в коллекцию или продукт'
        verbose_name_plural = 'Статистика перехода в коллекцию или продукт'


class Statistic_Find_Bloc(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    session_key = models.CharField(max_length=64, blank=True, null=True, default=None)
    collection = models.TextField(blank=True, null=True, default=None)
    page = models.CharField(max_length=10, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Статистика блочного поиска'
        verbose_name_plural = 'Статистика блочного поиска'


class Log_In_Site(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    session_key = models.CharField(max_length=64, blank=True, null=True, default=None)
    leng = models.CharField(max_length=3, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Статистика нахождения пользователей на сайте'
        verbose_name_plural = 'Статистика нахождения пользователей на сайте'


class Eye(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    session_key = models.CharField(max_length=64, blank=True, null=True, default=None)
    page = models.CharField(max_length=20, blank=True, null=True, default=None)
    log_in_site = models.ForeignKey(Log_In_Site, null=True, default=None)
    locate_product = models.BooleanField(default=False)
    locate_collection = models.BooleanField(default=False)
    locate_manafactur = models.BooleanField(default=False)
    send_project = models.BooleanField(default=False)
    send_project_id = models.CharField(max_length=20, blank=True, null=True, default=None)
    buy = models.BooleanField(default=False)
    buy_id = models.CharField(max_length=20, blank=True, null=True, default=None)


    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Слежение посещения'
        verbose_name_plural = 'Слежение посещения'
