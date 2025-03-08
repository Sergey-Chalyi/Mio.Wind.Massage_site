from django.contrib import admin

from servises.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'options', 'show_on_main', 'show_on_all_servises', 'priority', 'time_created', 'time_updated')
    list_display_links = ('title', )
    list_editable = ('show_on_main', 'show_on_all_servises', 'priority')

    search_fields = ('title', 'short_description')

    list_filter = [ 'show_on_main', 'show_on_all_servises']
