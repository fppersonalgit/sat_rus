from django.shortcuts import render, get_object_or_404
from .models import Project
from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    try:
        projects = Project.objects.all()
    except Project.DoesNotExist:
        raise Http404("Projects not found")
    return render(request, 'sat/base.html', context={'projects': projects})


def view_project(request, project_id):
    try:
        project_detail = Project.objects.get(project_id= project_id)
    except Project.DoesNotExist:
        raise Http404("Projects not found")
    return render(request, 'sat/base.html', context={'project_detail': project_detail})
