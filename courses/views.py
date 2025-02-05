from django.shortcuts import render
from django.http import HttpResponse

def kurslar(req):
    return HttpResponse( "kurs listesi")

def details(req, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getCoursesByCategory(req, category_name):
    text = ""
    if category_name == "web-gelistirme":
        text = "web gelistirme kategori sayfası"
    elif category_name == "proglamlama":
        text = "proglamlama kategori sayfası"
    else:
        text = "yanlış kategori seçimi"

    return HttpResponse(text)

def getCoursesByCategoryId(req, category_id):
    return HttpResponse(category_id)