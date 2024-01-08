from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Inventory'

urlpatterns=[
	path('inventory/', views.item_list, name='item_list'),
	path('inventory/<int:item_id>/', views.item_details, name='item_details'),
	path('<int:item_id>/transfer', views.transferitm, name='transferitm'),
	path('<int:item_id>/return', views.returnitm, name='returnitm'),
	path('rebuy-list/', views.rebuy_list, name='rebuy_list'),
	path('item/edit/<int:item_id>/', views.item_edit, name='item_edit'),
	path('item/delete/<int:item_id>/', views.item_delete, name='item_delete'),
	path('item/create/', views.item_create, name='item_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
