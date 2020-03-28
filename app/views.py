from django.shortcuts import render
from .models import Projects


def home(request):
    projects = Projects.objects.all()
    return render(request, 'index.html', {'prj': projects})
