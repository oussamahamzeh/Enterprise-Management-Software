
from django.contrib import admin

# Register your models here.

from .models import Document,Category

admin.site.register(Document)
admin.site.register(Category)

