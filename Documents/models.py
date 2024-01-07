from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime, timedelta

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Get the current datetime
        current_datetime = datetime.now()

        # Format the datetime as a string
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

        # Set the formatted datetime as the value for the field
        self.created_at = formatted_datetime

        super().save(*args, **kwargs)