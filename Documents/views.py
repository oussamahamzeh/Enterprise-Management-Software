from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import DocumentForm
from .models import Document
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Document, Category
from .forms import UploadDocumentForm

@login_required
def upload_document(request):
    if request.method == 'POST':
        form = UploadDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.owner = request.user
            document.save()
            messages.success(request, 'Document uploaded successfully.')
            return redirect('documents:document_list')
    else:
        form = UploadDocumentForm()
    categories = Category.objects.all()
    return render(request, 'upload_document.html', {'form': form, 'categories': categories})


def document_delete(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    if request.method == 'POST':
        document.delete()
        documents = Document.objects.all()
        categories = Category.objects.all()
        selected_category = request.GET.get('category', None)
        return redirect(reverse('documents:document_list'))
    return render(request, 'document_delete.html', {'document': document})

@login_required
def document_list(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category', None)
    if selected_category:
        documents = Document.objects.filter(category__category=selected_category)
    else:
        documents = Document.objects.all().order_by('-document_id')
    return render(request, 'document_list.html', {'documents': documents, 'categories': categories, 'selected_category': selected_category})

@login_required
def page(request):
    return render(request, 'page.html')
