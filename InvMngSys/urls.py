"""InvMngSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.admin import ModelAdmin
from django.contrib.admin.options import BaseModelAdmin
from django.urls import path, include
from django.contrib.auth import views as auth_views

import InvMngSys
from Inventory import views
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin
from InvMngSys.custom_admin import custom_admin_site
from django.urls import path
from django.contrib import admin

urlpatterns = [
                  path('', views.homepage, name='homepage'),
                  # path('', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
                  path('admin/', custom_admin_site.urls),
                  path('inventory/', include('Inventory.urls', namespace='inventory')),  # items/
                  path('documents/', include('Documents.urls', namespace='documents')),  # documents/
                  path('financials/', include('financials.urls', namespace='financials')),  # financials/
                  path('cashier/', include('cashier.urls', namespace='cashier')),  # cashier/
                  path('login/', auth_views.LoginView.as_view(), name='login'),
                  # path('', include('django.contrib.auth.urls')),

                  # path('', include('django.contrib.auth.urls')),#accounts/
                  # path('login/', views.login_view, name='login'),
                  # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
                  # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
