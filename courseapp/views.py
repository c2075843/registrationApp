from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from registrationapp.decorators import login_required_with_message
from .models import Module, Registration
from django.contrib.auth.models import Group
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    return render(request, "courseapp/home.html", {"title": "Home page"})


def about(request):
    return render(request, "courseapp/about.html", {"title": "About US"})


def contact(request):
    return render(request, "courseapp/contact.html", {"title": "Contact US"})

@login_required_with_message(message="You need to log in to access this page.")
def module_list(request):
    modules = Module.objects.all()
    return render(request, "courseapp/module_list.html", {"modules": modules})


def module_detail(request, code):
    module = get_object_or_404(Module, code=code)
    registered_students = Registration.objects.filter(module=module).select_related('student__user')
    module.registered_students = registered_students
    # Check if the user is registered for this module
    registered = False
    if request.user.is_authenticated:
        registered = Registration.objects.filter(
            student=request.user.student, module=module
        ).exists()
    context = {
        'module': module,
        "registered": registered, 
        'registered_students': registered_students 
        }
    return render(request, 'courseapp/module_detail.html', context)

@login_required_with_message(message="You need to log in to access this page.")
def registrations(request):
    modules = Module.objects.all()
    for module in modules:
        registered_students = Registration.objects.filter(module=module).select_related('student__user')
        module.registered_students = registered_students

        # Check if the user is registered for this module and attach the result to the module object
        module.is_registered = False
        if request.user.is_authenticated:
            module.is_registered = Registration.objects.filter(
                student=request.user.student, module=module
            ).exists()

    paginator = Paginator(modules, 1)  # Display 1 module per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }

    if request.method == 'POST':
        module_code = request.POST.get('module_code')
        try:
            module = Module.objects.get(code=module_code)
        except Module.DoesNotExist:
            return redirect('courseapp:registrations')  # Redirect to the same page if the module does not exist

        if request.user.is_authenticated:
            if 'register' in request.POST:
                Registration.objects.create(student=request.user.student, module=module)
            elif 'unregister' in request.POST:
                Registration.objects.filter(student=request.user.student, module=module).delete()

        return redirect('courseapp:registrations')  # Redirect to the same page after registration/unregistration

    return render(request, "courseapp/registrations.html", context)

@login_required_with_message(message="You need to log in to access this page.")
def course_detail(request, pk):
    course = get_object_or_404(Group, pk=pk)
    modules = course.modules.all()
    context = {"course": course, "modules": modules}
    return render(request, "courseapp/course_detail.html", context)



@login_required_with_message(message="You need to log in to access this page.")
def register_view(request, code):
    module = Module.objects.get(code=code)
    student = request.user.student
    registration, created = Registration.objects.get_or_create(
        student=student, module=module
    )
    if created:
        messages.success(request, f"You have registered for {module.name}")
        return redirect(
            reverse("courseapp:module_detail", args=[code])
        )  # Redirect to the desired page after registration
    else:
        messages.warning(request, "Something went wrong")


@login_required_with_message(message="You need to log in to access this page.")
def unregister_view(request, code):
    module = Module.objects.get(code=code)
    registration = Registration.objects.filter(
        student=request.user.student, module=module
    )
    if registration.exists():
        registration.delete()
        messages.warning(request, "Unregister succesful")
        return redirect(reverse("courseapp:module_detail", args=[code]))
    else:
        messages.warning(request, "Unregister failed")
