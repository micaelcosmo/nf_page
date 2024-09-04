"""
URL configuration for portal_nf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from navigate import views


urlpatterns = [
    # COMMON USER
    path('', views.index, name='index'),
    path('horarios/', views.class_schedules, name='class_schedules'),
    path('experimental_class/', views.experimental_class, name='experimental_class'),

    # SUPER USER
    path('admin/', admin.site.urls),
    path('class_schedules/management/', views.manage_class_schedules, name='manage_class_schedules'),
    path('request_experimental_class/', views.request_experimental_class, name='request_experimental_class'),

    # LOGIN
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
