from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    return HttpResponse( "anasayfa")

def hakkimizda(req):
    return HttpResponse("hakkimizda sayfası")

def iletisim(req):
    return HttpResponse("iletiişim sayfasi")
