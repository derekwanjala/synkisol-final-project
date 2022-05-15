from django.shortcuts import get_object_or_404, render

from .models import Project

def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})
