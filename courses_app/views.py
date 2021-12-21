from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, "index.html", context)

def add_course(request):
    # assign values to new obj
    add_obj = Course.objects.create(name=request.POST['name'],
    desc=Description.objects.create(notes=request.POST['desc'])
    )
    return redirect("/")

def del_page(request, _id):
    context = {
        'course':Course.objects.get(id=_id)
    }
    return render(request, "del_pg.html", context)
    # ^^^HOW DO I NEED TO SET UP THIS RETURN STMT????

def destroy(request, _id):
    course_to_delete = Course.objects.get(id=_id)
    course_to_delete.delete()
    return redirect("/")
