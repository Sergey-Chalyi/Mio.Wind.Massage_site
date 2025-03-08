from django.http import HttpRequest
from django.shortcuts import redirect, render

from map.models import MapPageInfo
from homepage.forms import AddVisitRecordForm
from homepage.models import FAQ, CompanySocials, FooterBlock, GenInfoBlock, Logo, OtherPagesMainPhotos
from sertificates.models import SertificateForSum, Subscription
from employees.models import Comment, Employee
from servises.models import Service


def page_map(request: HttpRequest):
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
    rights = FooterBlock.objects.all()
    gen_info_block = GenInfoBlock.objects.all()
    page_photo = OtherPagesMainPhotos.objects.filter(page_name='map').first()
    maps = MapPageInfo.objects.all()

    
    data = {
        'logo' : logo,
        'socials' : socials,
        'altegio_social' : altegio_social,
        'rights' : rights,
        'gen_info_block' : gen_info_block,
        'page_photo' : page_photo,
        'maps' : maps,

        'form' : form,
    }
    
    return render(request, 'pages/map/page-map.html', data)
