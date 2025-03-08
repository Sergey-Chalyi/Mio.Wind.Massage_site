"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

import homepage.views
import servises.views
import employees.views
import sertificates.views
import map.views
import pp.views


urlpatterns = [
    path('admiiiiin0298384/', admin.site.urls),

    path('', homepage.views.homepage, name='homepage'),
    path("servises/", servises.views.page_servises, name="page_servises"),
    path("employees/", employees.views.page_employees, name="page_employees"),
    path("employees/<slug:employee_slug>/", employees.views.page_certain_employee, name='employee_profile'),
    path("subscriptions-and-sertificates/", sertificates.views.page_subscriptions_and_sertificates, name='page_subscriptions_and_sertificates'),
    path("map/", map.views.page_map, name='page_map'),
    path("privacy-policy/", pp.views.page_pp, name='page_pp'),

] 


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = 'Адміністративна панель'
admin.site.index_title = 'Mio.Wind.Massage'