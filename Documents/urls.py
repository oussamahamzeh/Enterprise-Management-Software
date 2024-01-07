from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_document, document_list, page
from . import views

app_name = 'documents'

urlpatterns = [
                  # path('', home, name='home'), # Home page
                  path('upload/', views.upload_document, name='upload_document'),
                  path('documents/', views.document_list, name='document_list'),
                  #path('document_list/', views.document_list, name='document_list'),
                  path('documents/delete/<int:document_id>/', views.document_delete, name='document_delete'),
                  path('', page, name='page'),  # page/

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
