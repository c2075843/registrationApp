from django.urls import reverse
from django.shortcuts import render, redirect

from registrationapp.decorators import login_required_with_message
from .forms import UserUpdateForm, UserRegisterForm
from django.contrib import messages
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


@login_required_with_message(message="You need to log in to access this page.")
def profile(request):
    student = request.user.student

    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=student)
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("accounts:profile")
    else:
        p_form = ProfileUpdateForm(instance=student)
        u_form = UserUpdateForm(instance=request.user)

    context = {"student": student, "p_form": p_form, "u_form": u_form}

    # Disable the course field if user already has a course assigned
    if student.course:
        p_form.fields["course"].widget.attrs["disabled"] = True

    return render(request, "accounts/profile.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Your account has been created! Now you can login!"
            )
            return redirect("accounts:login")
        else:
            messages.warning(request, f"Unable to create account!")
        return redirect("courseapp:home")
    else:
        form = UserRegisterForm()
        return render(request, "accounts/register.html", {"form": form})


@login_required_with_message(message="You need to log in to access this page.")
def my_registrations(request):
    # import pdb

    # pdb.set_trace()
    context = {"registered_modules": request.user.student.student_registrations}
    return render(request, "accounts/my_registrations.html", context)


class CustomPasswordResetView(PasswordResetView):
    email_template_name = "password_reset_email.html"
    subject_template_name = "mail_subject.txt"
    template_name = "password_reset_form.html"

    def get_success_url(self):
        return reverse("password_reset_done")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "password_reset_confirm.html"
    def get_success_url(self):
        return reverse("login")


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "password_reset_complete.html"
