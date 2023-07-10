
from django.urls import path,include
from courseapp import views

app_name="courseapp"

#URL Configurations
urlpatterns = [
    path("", views.home, name="home"),   
]
