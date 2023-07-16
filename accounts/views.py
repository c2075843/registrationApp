
from django.shortcuts import render,redirect
from .forms import UserUpdateForm,UserRegisterForm
from django.contrib import messages
from accounts.models import Student
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm


@login_required
def profile(request):
    student = request.user.student

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=student)

    context = {
        'student': student,
        'form': form
    }

    return render(request, 'accounts/profile.html', context)


def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
              form.save()
              messages.success(request, f'Your account has been created! Now you can login!')
              return redirect('accounts:login')
        else:
              messages.warning(request, f'Unable to create account!')
        return redirect('courseapp:home')
    else:
        form= UserRegisterForm()
        return render(request,'accounts/register.html', {'form':form})
