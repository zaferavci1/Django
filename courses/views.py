from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import course



data = {
    "programlama" : "proglamlama kategorisine ait kurslar",
    "web-gelistirme" : "web gelistirme kategorisine ait kurslar",
    "mobil-uygulamalar" : "mobil kategorisine ait kurslar",
}

db = {
    "courses":[
        {
            "title":"javascript kursu",
            "description":"javascript kursu açıklama",
            "imageUrl":"1.jpg",
            "slug":"javascript-",
            "date": date(2024,6,19),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title":"pyhton kursu",
            "description":"pyhton kursu açıklama",
            "imageUrl":"2.jpg",
            "slug":"pyhton-",
            "date": date(2024,5,19),
            "isActive": False,
            "isUpdated": True
        },
        {
            "title":"web-gelistirme kursu",
            "description":"web-gelistirme kursu açıklama",
            "imageUrl":"3.jpg",
            "slug":"web-gelistirme-",
            "date": date(2024,4,19),
            "isActive": True,
            "isUpdated": True
        }
    ],
    "categories":[
        {"id":1, "name":"programlama", "slug":"programlama"},
        {"id":2, "name":"web gelistirme", "slug":"web-gelistirme"},
        {"id":3, "name":"mobil uygulamalar", "slug":"mobil-uygulamalar"}
        ]
}


def index(req):
    kurslar = course.objects.filter(isActive=1)
    kategoriler = db["categories"]
    return render(req, "courses/index.html", {
        'categories': kategoriler,
        'courses': kurslar
    })

def details(req, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getCoursesByCategory(req, category_name):
    try:
        category_text = data[category_name]
        return render(req, "courses/courses.html", {
            'category':category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound("sayfa bulunamadı")

def getCoursesByCategoryId(req, category_id):
    category_list = list(data.keys())
    if (category_id > len(category_list)):
        return HttpResponseNotFound("yanlış kategori seçimi")
    
    category_name = category_list[category_id - 1]

    redirect_url = reverse("courses_by_category", args=[category_name])
    return redirect(redirect_url)
    
    
