from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from app.models import *

def Base(request):
    return render(request, 'base.html')

@login_required
def Home(request):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')
    
    context = {
        'category': category,
        'course': course,
    }

    return render(request, 'Main/home.html', context)

@login_required
def Single_Course(request):
    category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    context = {
        'category': category,
        'level': level,
        'course': course,
    }
    return render(request, 'Main/single_course.html',context)

def About_Us(request):
    category = Categories.get_all_category(Categories)
    
    context = {
        'category': category,
    }
    return render(request, 'Main/about_us.html',context)

def Contact_Us(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category': category,
    }
    return render(request, 'Main/contact_us.html',context)

def Course_Details(request,slug):
    course = Course.objects.filter(slug = slug)
    if course.exists():
        course = course.first()
    else:
        return redirect('404')
    context = {
        'course': course,
    }
    return render(request, 'course/course_details.html',context)

def PageNotFound(request):
    return render(request, '404.html')