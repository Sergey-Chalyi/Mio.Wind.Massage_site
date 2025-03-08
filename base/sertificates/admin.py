from django.contrib import admin
from sertificates.models import Subscription, SertificateForSum, SubscriptionsPageinfo, SertificatesPageinfo


@admin.register(SubscriptionsPageinfo)
class SubscriptionsPageinfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_created', 'time_updated')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'phrase', 'durations', 'counts', 'discount_info', 'time_created', 'time_updated')
    list_display_links = ('name', )
    list_editable = ('phrase', )

    search_fields = ('name', 'phrase', 'discount_info')



@admin.register(SertificatesPageinfo)
class SertificatesPageinfoAdmin(admin.ModelAdmin):
    filter_horizontal = ['popular_servises']


@admin.register(SertificateForSum)
class SertificateForSumAdmin(admin.ModelAdmin):
    list_display = ('price', 'time_created', 'time_updated')
    list_display_links = ('price', )

    search_fields = ('price', )

