import os
import shutil

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime, timedelta

from django.db.models.signals import post_delete, pre_save, post_save
from django.dispatch import receiver
from django import forms

from InvMngSys.settings import MEDIA_ROOT


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


def document_upload_to(instance, filename):
    # Upload to 'documents/<document_id>/<filename>'
    return f'documents/{DocumentNumber.get_current_document_id()}/{filename}'


class DocumentNumber(models.Model):
    value = models.IntegerField(default=0)

    @classmethod
    def get_current_document_id(cls):
        counter, created = cls.objects.get_or_create(pk=1)
        return counter.value

    @classmethod
    def get_next_document_id(cls):
        counter, created = cls.objects.get_or_create(pk=1)
        if not created:
            counter.value += 1
            counter.save()
        return counter.value

    # You can use this function in a python shell:
    # Start the virtual environment -> go to the main path
    # python manage.py shell
    # from Documents.models import DocumentNumber
    # DocumentNumber.reset_document_id(new_value=your_desired_value)
    @classmethod
    def reset_document_id(cls, new_value=0):
        counter, created = cls.objects.get_or_create(pk=1)
        counter.value = new_value
        counter.save()


class Document(models.Model):
    document_id = models.IntegerField(primary_key=True, default=None, unique=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=document_upload_to)
    created_at = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Ensure document_id is set only if it's not already set
        if self.document_id is None:
            self.document_id = DocumentNumber.get_next_document_id()
        # Get the current datetime
        current_datetime = datetime.now()

        # Format the datetime as a string
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

        # Set the formatted datetime as the value for the field
        self.created_at = formatted_datetime

        super().save(*args, **kwargs)


@receiver(post_delete, sender=Document)
def delete_folder(sender, instance, **kwargs):
    folder_path = os.path.join(MEDIA_ROOT, 'documents', str(instance.document_id))
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
