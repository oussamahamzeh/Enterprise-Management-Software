# dashboard/views.py
from django.shortcuts import render

def dashboard_view(request):
    # Your dashboard logic goes here
    return render(request, 'dashboard/dashboard.html')
