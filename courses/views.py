from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return HttpResponse( "anasayfa")

def kurslar(req):
    return HttpResponse( "kurs listesi")
