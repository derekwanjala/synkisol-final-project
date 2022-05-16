from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import About, Clients, Company, Service, Strategy
from project.models import Project

def home(request):
    company = Company.objects.get(pk=1)
    about = About.objects.all()
    service = Service.objects.order_by('-created')[:4]
    projects = Project.objects.order_by('-created')[:6]
    clients = Clients.objects.all()
    return render(request, 'index.html', {'company': company, 'about': about, 'service': service, 'projects': projects, 'clients': clients})


def about(request):
    company = Company.objects.get(pk=1)
    about = About.objects.all()
    clients = Clients.objects.all()
    return render(request, 'about.html', {'company': company, 'about': about, 'clients': clients})


def service(request):
    service = Service.objects.all()
    return render(request, 'service.html', {'service': service})



class ServiceDetail (generic.DetailView):
    model = Service
    template_name = 'service_detail.html'
