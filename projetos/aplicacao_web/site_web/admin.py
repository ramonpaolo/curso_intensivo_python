from django.contrib import admin

from site_web.models import Topic
from site_web.models import Entry

admin.site.register(Topic)
admin.site.register(Entry)