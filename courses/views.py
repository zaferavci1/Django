from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



data = {
    "proglamlama" : "proglamlama kategorisine ait kurslar",
    "web-gelistirme" : "web gelistirme kategorisine ait kurslar",
    "mobil" : "mobil kategorisine ait kurslar",
}

def index(req):
    return render(req, "courses/index.html")

def kurslar(req):
    list_items = ""
    category_list = list(data.keys())

    for cat in category_list:
        redirect_url = reverse("courses_by_category", args=[cat])
        list_items += f"<li><a href='{redirect_url}'> {cat}</a></li>"
    
    html = f"<h1>kurs listesi</h1></br><ul>{list_items}</ul>"
    return HttpResponse(html)

def details(req, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getCoursesByCategory(req, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("sayfa bulunamadı")

def getCoursesByCategoryId(req, category_id):
    category_list = list(data.keys())
    if (category_id > len(category_list)):
        return HttpResponseNotFound("yanlış kategori seçimi")
    
    category_name = category_list[category_id - 1]

    redirect_url = reverse("courses_by_category", args=[category_name])
    return redirect(redirect_url)
    
    
