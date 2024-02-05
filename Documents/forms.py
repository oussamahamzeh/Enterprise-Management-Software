from django import forms
from .models import Document, Category


class UploadDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'file', 'category')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'file')#, 'document_id')
