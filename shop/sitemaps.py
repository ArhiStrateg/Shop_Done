from django.contrib.sitemaps import Sitemap
from products.models import Collection
from datetime import datetime, date, time, timedelta

from django.urls import reverse


class SitemapXML(Sitemap):
    changefreq = 'yearly'
    priority = 0.8

    def items(self):
        return Collection.objects.filter().order_by('id_patch')

    def lastmod(self, obj):
        create = datetime.now()
        create = datetime.today() - timedelta(days=10)
        # create_now = datetime.now()
        # create_date = datetime.date(create_now)
        # create_time = datetime.time(create_now)
        # create = create.isoformat(sep='T')
        # return "2018-04-26T14:23:36+00:00"
        return create


    def location(self, obj):
        return "/catalog/%s/" % obj.id_patch


class SitemapXL(Sitemap):
    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['main', 'zakaz', 'company', 'contacts']

    def location(self, item):
        return reverse(item)