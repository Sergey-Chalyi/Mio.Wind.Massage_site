from django.contrib import admin

from homepage.models import FAQ, CompanySocials, FooterBlock, Logo, OtherPagesMainPhotos, PrivacyPolicy, VisitRecord, WelcomeBlock, GenInfoBlock, AboutAsBlock, GeneralBenefitsBlock, AdvantagesBlock


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('text', 'time_created', 'time_updated')
    list_display_links = ('text',)


@admin.register(CompanySocials)
class CompanySocialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_created', 'time_updated')
    list_display_links = ('title',)
    search_fields = ('title',)


@admin.register(WelcomeBlock)
class WelcomeBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_created', 'time_updated')
    list_display_links = ('title',)


@admin.register(GenInfoBlock)
class GenInfoBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'time_created', 'time_updated')
    list_display_links = ('title', )

    list_editable = ('text', )

    search_fields = ('title', 'text')


@admin.register(AboutAsBlock)
class AboutAsBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'time_created', 'time_updated')
    list_display_links = ('title', )


@admin.register(GeneralBenefitsBlock)
class GeneralBenefitsBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'time_created', 'time_updated')
    list_display_links = ('title', )

    search_fields = ('title', 'text')


@admin.register(AdvantagesBlock)
class AdvantagesBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'time_created', 'time_updated')
    list_display_links = ('title', )

    search_fields = ('title', 'text')


@admin.register(FooterBlock)
class FooterBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_created', 'time_updated')
    list_display_links = ('title', )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time_created', 'time_updated')
    list_display_links = ('title', )

    search_fields = ('title', 'description')


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    pass


@admin.register(OtherPagesMainPhotos)
class OtherPagesMainPhotosAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title', 'time_created', 'time_updated')
    list_display_links = ('page_name', )

    list_editable = ('title', )

    search_fields = ('page_name', 'title')


@admin.register(VisitRecord)
class VisitRecordAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_tel', 'customer_comment', 'is_processed', 'time_created', 'time_updated')

    list_display_links = ('customer_name', 'customer_tel')

    list_editable = ('is_processed',)

    search_fields = ('customer_name', 'customer_tel', 'customer_comment')

    list_filter = ['is_processed']
