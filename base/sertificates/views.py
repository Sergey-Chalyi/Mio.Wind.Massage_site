from django.http import HttpRequest
from django.shortcuts import redirect, render

from homepage.forms import AddVisitRecordForm
from homepage.models import FAQ, CompanySocials, FooterBlock, GenInfoBlock, Logo, OtherPagesMainPhotos
from sertificates.models import SertificateForSum, SertificatesPageinfo, Subscription, SubscriptionsPageinfo
from employees.models import Comment, Employee
from servises.models import Service


def page_subscriptions_and_sertificates(request: HttpRequest):
    if request.method == 'POST':
        form = AddVisitRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_subscriptions_and_sertificates')
    else:
        form = AddVisitRecordForm()

    logo = Logo.objects.all()
    socials = CompanySocials.objects.all()
    altegio_social = socials.filter(title__iexact="altegio").first()
    rights = FooterBlock.objects.all()
    gen_info_block = GenInfoBlock.objects.all()
    page_photo = OtherPagesMainPhotos.objects.filter(page_name='servises').first()

    subscription_page_info = SubscriptionsPageinfo.objects.all()
    sertificates_page_info = SertificatesPageinfo.objects.all()
    
    all_services = Service.objects.all()
    subscriptions = Subscription.objects.all()
    sum_sertificates = SertificateForSum.objects.all()

    data = {
        'logo' : logo,
        'socials' : socials,
        'altegio_social' : altegio_social,

        'rights' : rights,

        'gen_info_block' : gen_info_block,
        'page_photo' : page_photo,

        'subscription_page_info' : subscription_page_info,
        'sertificates_page_info' : sertificates_page_info,

        'all_services' : all_services,
        'django_subscriptions' : subscriptions,
        'sum_sertificates' : sum_sertificates,
        'form' : form,
    }

    return render(request, 'pages/sertificates-and-subscriptions/page-sertificates-and-subscriptions.html', data)
