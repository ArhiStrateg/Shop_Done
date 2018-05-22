from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import *
from shop.sitemaps import SitemapXML, SitemapXL
from django.contrib.sitemaps.views import sitemap

from django.contrib.sitemaps import GenericSitemap, Sitemap


admin.autodiscover()

sitemaps = {'static': SitemapXL, 'main': SitemapXML}

urlpatterns = [
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls')),
    url(r'^', include('products.urls')),
    url(r'^', include('orders.urls')),
    url(r'^', include('shadow.urls')),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),

] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)