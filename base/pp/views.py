from django.http import HttpRequest
from django.shortcuts import redirect, render

from homepage.forms import AddVisitRecordForm
from homepage.models import FAQ, CompanySocials, FooterBlock, GenInfoBlock, Logo, OtherPagesMainPhotos, PrivacyPolicy
from sertificates.models import SertificateForSum, Subscription
from employees.models import Comment, Employee
from servises.models import Service
from homepage.models import PrivacyPolicy


def page_pp(request: HttpRequest):
    if request.method == 'POST':
        form = AddVisitRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_pp')
    else:
        form = AddVisitRecordForm()
        pp = PrivacyPolicy.objects.all()

    logo = Logo.objects.all()
    socials = CompanySocials.objects.all()
    altegio_social = socials.filter(title__iexact="altegio").first()
    rights = FooterBlock.objects.all()
    gen_info_block = GenInfoBlock.objects.all()
    page_photo = OtherPagesMainPhotos.objects.filter(page_name='privacy policy').first()
    
    data = {
        'logo' : logo,
        'socials' : socials,
        'altegio_social' : altegio_social,
        'rights' : rights,
        'gen_info_block' : gen_info_block,
        'page_photo' : page_photo,

        'pp' : pp,
        'form' : form,
    }

    return render(request, 'pages/pp/page-pp.html', data)