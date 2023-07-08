from django.shortcuts import render


def home(request):
    return render(request, "courseapp/home.html", {"title": "Home page"})

