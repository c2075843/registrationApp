
from django.urls import path,include
from courseapp import views
from .views import module_list, module_detail


app_name="courseapp"

#URL Configurations
urlpatterns = [
    path("", views.home, name="home"), 
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('modules', module_list, name='module_list'),
    path('modules/<int:pk>/', module_detail, name='module_detail'),
    
    
]
