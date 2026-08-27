"""
URL configuration for djangoproyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

# 1. Importas las vistas de tu primera aplicación
from app_uno import views as vistas_uno 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 2. Registras las dos direcciones web para app_uno
    path('app-uno/inicio/', vistas_uno.inicio_app_uno),
    path('app-uno/detalle/', vistas_uno.detalle_app_uno),
]