from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect

from homepage.forms import AddVisitRecordForm
from homepage.models import FAQ, CompanySocials, FooterBlock, GenInfoBlock, Logo, OtherPagesMainPhotos
from sertificates.models import SertificateForSum, Subscription
from employees.models import Comment, Employee, EmployeesPageInfo
from servises.models import Service

from django.contrib import messages



def page_employees(request: HttpRequest):
    if request.method == 'POST':
        form = AddVisitRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_employees')
    else:
        form = AddVisitRecordForm()

    logo = Logo.objects.all()
    socials = CompanySocials.objects.all()
    altegio_social = socials.filter(title__iexact="altegio").first()

    rights = FooterBlock.objects.all()

    gen_info_block = GenInfoBlock.objects.all()

    employees = Employee.objects.filter(show_on_all_specialists=True).order_by('priority')
    employees_page_info = EmployeesPageInfo.objects.all()
    page_photo = OtherPagesMainPhotos.objects.filter(page_name='employees').first()
    

    data = {
        'logo' : logo,
        'socials' : socials,
        'altegio_social' : altegio_social,

        'rights' : rights,

        'gen_info_block' : gen_info_block,
        'employees_page_info' : employees_page_info,
        'employees' : employees,
        'page_photo' : page_photo,

        'form' : form
    }

    return render(request, 'pages/employees/page-employees.html', data)


def page_certain_employee(request: HttpRequest, employee_slug: str):
    if request.method == 'POST':
        form = AddVisitRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_employees')
    else:
        employee = get_object_or_404(Employee, slug=employee_slug)
        form = AddVisitRecordForm(initial={'to_specialist': employee.first_name})
    
    logo = Logo.objects.all()
    socials = CompanySocials.objects.all()
    altegio_social = socials.filter(title__iexact="altegio").first()

    rights = FooterBlock.objects.all()

    gen_info_block = GenInfoBlock.objects.all()

    page_photo = OtherPagesMainPhotos.objects.filter(page_name='employees').first()

    data = {
        'logo' : logo,
        'socials' : socials,
        'altegio_social' : altegio_social,

        'rights' : rights,

        'gen_info_block' : gen_info_block,
        'page_photo' : page_photo,

        'employee' : employee,
        'form' : form
    }

    return render(request, 'pages/employees/page-employee.html', data)
