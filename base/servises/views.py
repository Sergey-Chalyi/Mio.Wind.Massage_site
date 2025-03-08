from django.http import HttpRequest
from django.shortcuts import redirect, render

from homepage.models import CompanySocials, FooterBlock, GenInfoBlock, Logo, OtherPagesMainPhotos
from homepage.forms import AddVisitRecordForm
from servises.models import Service

def page_servises(request: HttpRequest):
    if request.method == 'POST':
        form = AddVisitRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_congratulations')
    else:
        form = AddVisitRecordForm()

    services_show_on_homepage = Service.objects.filter(show_on_all_servises=True).order_by('priority')
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

        'services_show_on_homepage' : services_show_on_homepage,
        'form' : form,
    }

    return render(request, 'pages/servises/page-servises.html', data)