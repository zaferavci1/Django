from datetime import date
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import course, category


def index(req):
    kurslar = course.objects.filter(isActive=1)
    kategoriler = category.objects.all()
    return render(req, "courses/index.html", {
        'categories': kategoriler,
        'courses': kurslar
    })

def details(req, slug):
    try:
        courses = course.objects.get(slug = slug)
    except:
        raise Http404()
    context = {
        "course": courses
    }
    return render(req, "courses/details.html", context)

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
    
    
