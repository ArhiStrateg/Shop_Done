"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from orders.views import checkout, checkout_ukr,\
    basket_adding, \
    checkout_order, checkout_order_ukr, \
    checkout_end, checkout_end_ukr, \
    phone_adding


urlpatterns = [
    url(r'^checkout/$', checkout, name='checkout'),
    url(r'^checkout_ukr/$', checkout_ukr, name='checkout_ukr'),

    url(r'^checkout_order/$', checkout_order, name='checkout_order'),
    url(r'^checkout_order_ukr/$', checkout_order_ukr, name='checkout_order_ukr'),

    url(r'^checkout_end/$', checkout_end, name='checkout_end'),
    url(r'^checkout_end_ukr/$', checkout_end_ukr, name='checkout_end_ukr'),

    url(r'^basket_adding/$', basket_adding, name='basket_adding'),

    url(r'^phone_adding/$', phone_adding, name='phone_adding'),

]