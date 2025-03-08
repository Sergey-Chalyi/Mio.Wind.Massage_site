from django.http import HttpRequest
from django.shortcuts import redirect, render

from map.models import MapPageInfo
from homepage.forms import AddVisitRecordForm
from homepage.models import FAQ, AboutAsBlock, CompanySocials, FooterBlock, GenInfoBlock, Logo, WelcomeBlock, GeneralBenefitsBlock, AdvantagesBlock
from sertificates.models import SertificateForSum, SertificatesPageinfo, Subscription, SubscriptionsPageinfo
from employees.models import Comment, Employee, EmployeesPageInfo
from servises.models import Service

from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe
import json

def homepage(request: HttpRequest):

    if request.method == 'POST':
        form = AddVisitRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_congratulations')
    else:
        form = AddVisitRecordForm()
    
    logo = Logo.objects.all()
    socials = CompanySocials.objects.all()
    altegio_social = socials.filter(title__iexact="altegio").first()
    

    welcome_block = WelcomeBlock.objects.all()
    gen_info_block = GenInfoBlock.objects.all()
    about_as_block = AboutAsBlock.objects.all()
    general_benefits = GeneralBenefitsBlock.objects.all()
    employees_page_info = EmployeesPageInfo.objects.all()
    advantages = AdvantagesBlock.objects.all()
    subscription_page_info = SubscriptionsPageinfo.objects.all()
    maps = MapPageInfo.objects.all()
    sertificates_page_info = SertificatesPageinfo.objects.all()
    
    rights = FooterBlock.objects.all()

    all_services = Service.objects.all()
    services_show_on_homepage = all_services.filter(show_on_main=True).order_by('priority')
    employees = Employee.objects.filter(show_on_homepage=True).order_by('priority')
    subscriptions_queryset  = Subscription.objects.all()
    sum_sertificates = SertificateForSum.objects.all()
    feedbacks = Comment.objects.filter(show_on_homepage=True)
    questions = FAQ.objects.all()


    data = {
        'logo' : logo,
        'socials' : socials,
        'altegio_social' : altegio_social,

        'welcome_block' : welcome_block,
        'gen_info_block' : gen_info_block,
        'about_as_block' : about_as_block,
        'general_benefits' : general_benefits,
        'employees_page_info' : employees_page_info,
        'advantages' : advantages,
        'subscription_page_info' : subscription_page_info,
        'maps' : maps,
        'sertificates_page_info' : sertificates_page_info,

        'rights' : rights,

        'all_services' : all_services,
        'services_show_on_homepage': services_show_on_homepage, 
        'employees' : employees,
        "django_subscriptions" : subscriptions_queryset,
        'sum_sertificates' : sum_sertificates,
        'feedbacks' : feedbacks,
        'questions' : questions,

        'form' : form
    }

    return render(request, 'pages/homepage/page-home.html', data)


def congratulations(request: HttpRequest):
    if request.method == 'POST':
        form = AddVisitRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_congratulations')
    else:
        form = AddVisitRecordForm()

    logo = Logo.objects.all()
    socials = CompanySocials.objects.all()
    altegio_social = socials.filter(title__iexact="altegio").first()
    gen_info_block = GenInfoBlock.objects.all()

    
    
    rights = FooterBlock.objects.all()


    data = {
        'logo' : logo,
        'socials' : socials,
        'altegio_social' : altegio_social,
        'gen_info_block' : gen_info_block,

        'rights' : rights,

        'form' : form
    }

    return render(request, 'pages/congratulations.html', data)
