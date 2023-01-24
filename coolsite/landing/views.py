from django.shortcuts import render
from .forms import Clients_phone



def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html', {'ph': 'static/images/dj-neo1.img'})


def contact(request):
    form = Clients_phone
    context = {'form': form}
    return render(request, 'contact.html', context=context)


def work(request):
    return render(request, 'work.html')


def secret_master(request):
    return render(request, 'blog.html')

