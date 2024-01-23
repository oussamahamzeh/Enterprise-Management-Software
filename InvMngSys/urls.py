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

from django.conf import settings
from django.conf.urls.static import static
from . import views
from InvMngSys.custom_admin import custom_admin_site
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import password_reset_confirm_custom

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin/', custom_admin_site.urls),
    path('inventory/', include('Inventory.urls', namespace='inventory')),  # items/
    path('documents/', include('Documents.urls', namespace='documents')),  # documents/
    path('financials/', include('financials.urls', namespace='financials')),  # financials/
    path('cashier/', include('cashier.urls', namespace='cashier')),  # cashier/
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', password_reset_confirm_custom, name='password_reset_confirm'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('invalid-link/', views.invalid_link, name='invalid_link'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

