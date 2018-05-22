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
from shadow.views import shadow, shadow_projects, shadow_orders, project_singl, order_singl, statistic, statistic_simple_find, \
    statistic_bloc_find, statistic_in, session_key_eye, time_delta, projects_and_orders, pars


urlpatterns = [
    url(r'^shadow/$', shadow, name='shadow'),
    url(r'^projects_and_orders/$', projects_and_orders, name='projects_and_orders'),

    url(r'^shadow_projects/$', shadow_projects, name='shadow_projects'),
    url(r'^project_singl/(?P<project_singl_id>\w+)/$', project_singl, name='project_singl'),
    url(r'^session_key_eye/(?P<session_key_eye_id>\w+)/$', session_key_eye, name='session_key_eye'),

    url(r'^shadow_orders/$', shadow_orders, name='shadow_orders'),
    url(r'^order_singl/(?P<order_singl_id>\w+)/$', order_singl, name='order_singl'),

    url(r'^statistic/$', statistic, name='statistic'),
    url(r'^statistic_simple_find/$', statistic_simple_find, name='statistic_simple_find'),
    url(r'^statistic_bloc_find/$', statistic_bloc_find, name='statistic_bloc_find'),
    url(r'^statistic_in/$', statistic_in, name='statistic_in'),
    url(r'^time_delta/$', time_delta, name='time_delta'),

    url(r'^pars/$', pars, name='pars'),

    # url(r'^media/shadow_projects/$', media_shadow_projects, name='media_shadow_projects'),

]


