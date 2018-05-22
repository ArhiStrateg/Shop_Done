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
from main.views import main, main_ukr,\
    search, search_ukr,\
    search_hight, search_hight_ukr,\
    diler_otdel, \
    contacts, contacts_ukr, \
    zakaz, zakaz_ukr, \
    company, company_ukr, \
    projects_materials, projects_materials_ukr, \
    robots, sitemap



urlpatterns = [
    url(r'^robots.txt$', robots, name="robots"),
    # url(r'^sitemap.html$', sitemap, name="sitemap"),

    url(r'^$', main, name='main'),
    url(r'^main_ukr/$', main_ukr, name='main_ukr'),

    url(r'^search/$', search, name='search'),
    url(r'^search_ukr/$', search_ukr, name='search_ukr'),

    url(r'^search_hight/$', search_hight, name='search_hight'),
    url(r'^search_hight_ukr/$', search_hight_ukr, name='search_hight_ukr'),

    url(r'^projects_materials/$', projects_materials, name='projects_materials'),
    url(r'^projects_materials_ukr/$', projects_materials_ukr, name='projects_materials_ukr'),

    url(r'^diler_otdel/$', diler_otdel, name='diler_otdel'),

    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^contacts_ukr/$', contacts_ukr, name='contacts_ukr'),

    url(r'^company/$', company, name='company'),
    url(r'^company_ukr/$', company_ukr, name='company_ukr'),

    url(r'^zakaz/$', zakaz, name='zakaz'),
    url(r'^zakaz_ukr/$', zakaz_ukr, name='zakaz_ukr'),

]


