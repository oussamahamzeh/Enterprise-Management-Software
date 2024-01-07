from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cashier'

urlpatterns = [
                  path('cashier/', views.cashier, name='cashier'),
                  path('search/', views.search_item, name='search_item'),
                  path('clear_results/', views.clear_results, name='clear_results'),
                  path('create_transactions/', views.create_transactions, name='create_transactions'),
                  path('wholesale/', views.wholesale, name='wholesale'),
                  path('wholesale_create_transactions/', views.wholesale_create_transactions, name='wholesale_create_transactions'),
                  path('wholesale_search/', views.wholesale_search_item, name='wholesale_search_item'),
              ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
