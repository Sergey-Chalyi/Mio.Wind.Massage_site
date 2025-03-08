from django.contrib import admin

from employees.models import Employee, Comment, EmployeesPageInfo



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'is_active', 'show_on_homepage', 'show_on_all_specialists', 'priority', 'slug', 'time_created', 'time_updated')
    list_display_links = ('id', 'first_name', 'last_name')
    list_editable = ('is_active', 'show_on_homepage', 'show_on_all_specialists', 'priority', 'slug')

    search_fields = ('first_name', 'last_name')

    list_filter = [ 'is_active', 'show_on_homepage', 'show_on_all_specialists']

    filter_horizontal = ['services']


@admin.register(EmployeesPageInfo)
class EmployeesPageInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_created', 'time_updated')
    list_display_links = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialist', 'stars_count', 'show_on_homepage', 'time_created', 'time_updated')
    list_display_links = ('first_name', 'last_name')
    list_editable = ('specialist', 'stars_count', 'show_on_homepage')

    search_fields = ('first_name', 'last_name')

    list_filter = [ 'specialist', 'stars_count', 'show_on_homepage']
