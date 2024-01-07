from django.urls import include
from django.urls import path


from django.urls import path
from . import views

app_name = 'financials'

from django.urls import path
from . import views


app_name = 'financials'


urlpatterns = [
    path('financials/', views.financials, name='financials'),
    path('financials/transaction_list/', views.transaction_list, name='transaction_list'),
    path('financials/balance_sheet/', views.balance_sheet, name='balance_sheet'),

    # path('transactions/<int:transaction_id>/', views.transaction_details, name='transaction_details'),
    # path('balance/', views.balance, name='balance'),
    # path('income_statement/', views.income_statement, name='income_statement'),
    # Invoices
]
