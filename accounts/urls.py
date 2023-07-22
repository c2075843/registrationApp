from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.models import Student
from . import views


app_name = "accounts"

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    path("my_registrations/", views.my_registrations, name="my_registrations"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path(
        "logout",
        auth_views.LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
    path("profile/<int:pk>/", views.profile, name="profile"),
]
