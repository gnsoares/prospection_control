"""prospection_control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#
# IMPORTS
#
# Django
from django.contrib import admin
from django.urls import include, path

# Project
from .views.closed_companies import closed_companies
from .views.dashboard import dashboard
from .views.favicon import favicon


#
# CODE
#
urlpatterns = [
    path('admin/', admin.site.urls),
    path('config/', include('config.urls')),
    path('prospection/', include('prospection.urls')),
    path('', dashboard, name='dashboard'),
    path('closed_companies/', closed_companies, name='closed_companies'),
    path('favicon.ico', favicon, name='favicon'),
]
