from django.contrib import admin

from map.models import MapPageInfo

@admin.register(MapPageInfo)
class MapPageInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_created', 'time_updated')