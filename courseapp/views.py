from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Module, Registration
from django.contrib.auth.models import Group
from django.contrib import messages 


def home(request):
    return render(request, "courseapp/home.html", {"title": "Home page"})

def about(request):
    return render(request, 'courseapp/about.html',{'title': 'About US'})

def contact(request):
    return render(request, 'courseapp/contact.html',{'title': 'Contact US'})


def module_list(request):
    modules = Module.objects.all()
    return render(request, 'courseapp/module_list.html', {'modules': modules})

@login_required
def module_detail(request, pk):
    module = get_object_or_404(Module, pk=pk)
    registered_users_count = Registration.objects.filter(module=module).count()
    registered_students = Registration.objects.filter(module=module).values_list('student__user__first_name', 'student__user__last_name')
    

    if request.user.is_authenticated:
        registered = Registration.objects.filter(student=request.user.student, module=module).exists()

    context = {
        'module': module,
        'registered': registered,
        'registered_users_count': registered_users_count,
        'registered_students': registered_students
        
    }
    return render(request, 'courseapp/module_detail.html', context)

def course_detail(request, pk):
    course = get_object_or_404(Group, pk=pk)
    modules = course.modules.all()
    context = {'course': course, "modules":modules}
    return render(request, 'courseapp/course_detail.html', context)

@login_required
def register_view(request, module_id):
    module = Module.objects.get(pk=module_id)
    student= request.user.student
    registration,created=Registration.objects.get_or_create(student=student,module=module)
    if created:
       messages.success(request,f"You have registered for {module.name}")
       return redirect(reverse('courseapp:module_detail',args=[module_id]))  # Redirect to the desired page after registration
    else:
        messages.warning(request,"Something went wrong")

@login_required
def unregister_view(request, module_id):
    module = Module.objects.get(pk=module_id)
    registration= Registration.objects.filter(student=request.user.student, module=module)
    if registration.exists():
        registration.delete()
        messages.warning(request,"Unregister succesful")
        return redirect(reverse('courseapp:module_detail', args=[module_id]))
    else: 
        messages.warning(request,"Unregister failed")


    




