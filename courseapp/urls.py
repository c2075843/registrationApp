
from django.urls import path,include
from courseapp import views




app_name="courseapp"

#URL Configurations
urlpatterns = [
    path("", views.home, name="home"), 
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('modules', views.module_list, name='module_list'),
    path('module/<int:pk>/', views.module_detail, name='module_detail'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('register/<int:module_id>/', views.register_view, name='register'),
    path('unregister/<int:module_id>/', views.unregister_view, name='unregister'),
]
