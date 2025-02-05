from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect



data = {
    "proglamlama" : "proglamlama kategorisine ait kurslar",
    "web-gelistirme" : "web gelistirme kategorisine ait kurslar",
    "mobil" : "mobil kategorisine ait kurslar",
}

def kurslar(req):
    return HttpResponse( "kurs listesi")

def details(req, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getCoursesByCategory(req, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("sayfa bulunamadı")

def getCoursesByCategoryId(req, category_id):
    try:
        category_list = list(data.keys())
        redirect_text = category_list[category_id - 1]
        return redirect("/kurs/kategori/" + redirect_text)
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")