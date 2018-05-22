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
from products.views import collection, products, \
    manufacturer, manufacturer_ukr, \
    manufacturer_singl, manufacturer_singl_ukr, \
    collection_singl, collection_singl_ukr, \
    products_singl, products_singl_ukr, \
    collection_singl_project, collection_singl_project_ukr



urlpatterns = [
    url(r'^manufacturer/$', manufacturer, name='manufacturer'),
    url(r'^manufacturer_ukr/$', manufacturer_ukr, name='manufacturer_ukr'),
    url(r'^manufacturer_singl/(?P<manufacturer_singl_id>\w+)/$', manufacturer_singl, name='manufacturer_singl'),
    url(r'^manufacturer_singl_ukr/(?P<manufacturer_singl_id_ukr>\w+)/$', manufacturer_singl_ukr, name='manufacturer_singl_ukr'),

    url(r'^collection/$', collection, name='collection'),

    url(r'^catalog/(?P<id_patch>\w+)/$', collection_singl, name='collection_singl'),
    # url(r'^(?P<name_collection_re>\w+)/$', collection_singl, name='collection_singl'),

    url(r'^collection_singl_ukr/(?P<collection_singl_id_ukr>\w+)/$', collection_singl_ukr, name='collection_singl_ukr'),
    url(r'^collection_singl_project/(?P<collection_singl_id>\w+)/$', collection_singl_project,
        name='collection_singl_project'),
    url(r'^collection_singl_project_ukr/(?P<collection_singl_id_ukr>\w+)/$', collection_singl_project_ukr,
        name='collection_singl_project_ukr'),


    url(r'^products/$', products, name='products'),
    url(r'^products_singl/(?P<products_singl_id>\w+)/$', products_singl, name='products_singl'),
    url(r'^products_singl_ukr/(?P<products_singl_id_ukr>\w+)/$', products_singl_ukr, name='products_singl_ukr'),

]