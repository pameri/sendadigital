# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):    
    return render(request,'main/home.html',{})


def solicitud(request):    
    return render(request,'main/certificado_fe.html',{})

def senda(request):    
    return render(request,'main/index_senda.html',{})