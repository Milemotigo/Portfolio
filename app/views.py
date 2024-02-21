from django.shortcuts import render, redirect
from .forms import ClientForm


def index(request):
    if request.method=='POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            print('form saved successful')
            return redirect('')
    else:
        form = ClientForm()

    return render(request, 'index.html', locals())
