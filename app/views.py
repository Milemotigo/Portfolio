from django.shortcuts import render, redirect
from .forms import ClientForm
from . models import Client

def index(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            print('Form submission successful')
            return redirect('index')
        else:
            print('Form submission not successful', form.error)
    else:
        ClientForm()
    return render(request, 'index.html', locals())

def queryconnects(request):
    data = Client.objects.all()
    if data:
        print(data)
    else:
        print(data.error)
