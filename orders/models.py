from django.db import models
from products.models import Product
from django.db.models.signals import post_save


class Status(models.Model):
    name_status = models.CharField(max_length=48, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % (self.id)

    class Meta:
        verbose_name = 'Статус ордера'
        verbose_name_plural = 'Статусы ордера'

class Order(models.Model):
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, blank=True, null=True, default=None)
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Ордер на покупкуr'
        verbose_name_plural = 'Ордеры на покупку'

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s, %s" % (self.id, self.nmb)

    class Meta:
        verbose_name = 'Товар в ордере'
        verbose_name_plural = 'Товары в ордере'


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s, %s, %s" % (self.product.name_product, self.is_active, self.id)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):

        super(ProductInBasket, self).save(*args, **kwargs)


class Find_Project(models.Model):
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    session_key = models.CharField(max_length=64, null=True, default=None)

    status = models.ForeignKey(Status, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    project = models.FileField(upload_to='projects/')

    def __str__(self):
        return "%s, %s, %s" % (self.customer_name, self.customer_phone, self.created)

    class Meta:
        verbose_name = 'Спецификация на просчет'
        verbose_name_plural = 'Спецификации на просчет'

    def save(self, *args, **kwargs):
        super(Find_Project, self).save(*args, **kwargs)


class Call_Me(models.Model):
    call_me_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    call_me_phone = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % (self.id)

    class Meta:
        verbose_name = 'Перезвоните мне'
        verbose_name_plural = 'Перезвоните мне'

