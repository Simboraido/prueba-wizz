"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from users.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls), # Viene por defecto en Django
    
    # Endpoints de Autenticación
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', TokenObtainPairView.as_view(), name='signin'),


    # Endpoints de Tareas
    path('tasks/', include('tasks.urls')), # <-- Conectamos las rutas de tareas
]