
from django.shortcuts import render,redirect
from .forms import UserUpdateForm,UserRegisterForm
from django.contrib import messages


def profile(request):
    return render(request,'accounts/profile.html')


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
