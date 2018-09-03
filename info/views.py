from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import RegisteredInfo
from info import models

def index(request):
    return render(request, 'index.html')
   

def lists(request):
    info = models.information.objects.all()
    return render(request, 'list.html', {'info': info})

def adds(request):
    if request.method == 'POST':
        form_data = RegisteredInfo(request.POST)
        if form_data.is_valid():
            info = models.information()
            info.name  = form_data.cleaned_data['name']
            info.email = form_data.cleaned_data['email']
            info.save()
    else:
        form_data = RegisteredInfo()
    return render(request, 'add.html', {'form_data': form_data})
