from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from home.models import Service

def home(request):
    return HttpResponse("Hello Django")


def service(request):
    service = Service.objects.all()
    return render(request, 'service.html', {'service': service})



class ServiceDetail (generic.DetailView):
    model = Service
    template_name = 'service_detail.html'
