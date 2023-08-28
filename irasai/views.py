from django.shortcuts import render
from .models import Artistas, Irasai
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic



# Create your views here.
def index(request):
    numb_irasai = Irasai.objects.all().count()
    numb_of_artistai = Artistas.objects.count()

    context_t = {
        'numb_irasai_t': numb_irasai,
        'numb_of_artistai_t': numb_of_artistai,
    }

    return render(request, 'index.html', context=context_t)

def visi_artistai(request):
    artistai = Artistas.objects.all()
    context_t = {
        'artistai_t': artistai,
    }

    return render(request, 'artistai_visi.html', context=context_t)
