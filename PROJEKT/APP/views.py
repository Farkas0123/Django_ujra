from re import template
from django.shortcuts import render
from random import random, randint
from .models import Kerdes
# Create your views here.

def bigyoview (request):
    kerdesek = Kerdes.objects.all()

    # for kerdes in kerdesek:
    #     print(kerdes)


    template = 'bigyotemplate.html'
    context = {'a' : randint(0,10), 'kerdesek': kerdesek}
    return render(request,  template, context)