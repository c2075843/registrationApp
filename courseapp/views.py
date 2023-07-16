from django.shortcuts import get_object_or_404, render
from .models import Module
from django.contrib.auth.models import Group


def home(request):
    return render(request, "courseapp/home.html", {"title": "Home page"})

def about(request):
    return render(request, 'courseapp/about.html',{'title': 'About US'})

def contact(request):
    return render(request, 'courseapp/contact.html',{'title': 'Contact US'})


def module_list(request):
    modules = Module.objects.all()
    return render(request, 'courseapp/module_list.html', {'modules': modules})

def module_detail(request, pk):
    module = get_object_or_404(Module, pk=pk)
    context = {'module': module}  # Use 'module' instead of 'modules'
    return render(request, 'courseapp/module_detail.html', context)

def course_detail(request, pk):
    course = get_object_or_404(Group, pk=pk)
    modules = course.modules.all()
    context = {'course': course, "modules":modules}
    return render(request, 'courseapp/course_detail.html', context)