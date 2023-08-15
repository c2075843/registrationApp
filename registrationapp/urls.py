"""
URL configuration for registrationapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from courseapp.views import ApiRoot,CoursesList,ModulesList,RegistrationsList,UsersList,StudentsList
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("courseapp.urls")),
    path("accounts/", include("accounts.urls")),
path(
        "password_reset/",
        views.CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        views.CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path('api/',ApiRoot.as_view(),name=ApiRoot.name),
    path('api/students/', StudentsList.as_view(), name=StudentsList.name),
    path('api/users/', UsersList.as_view(), name=UsersList.name),
    path('api/courses/', CoursesList.as_view(), name=CoursesList.name),
    path('api/modules/', ModulesList.as_view(), name=ModulesList.name),
    path('api/registration/', RegistrationsList.as_view(), name=RegistrationsList.name),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
