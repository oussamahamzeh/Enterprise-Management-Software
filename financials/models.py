from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class TransactionExportNumber(models.Model):
    value = models.IntegerField(default=0)

    @classmethod
    def get_next_export_number(cls):
        counter, created = cls.objects.get_or_create(pk=1)
        if not created:
            counter.value += 1
            counter.save()
        return counter.value

    # You can use this function in a python shell:
    # Start the virtual environment -> go to the main path
    # python manage.py shell
    # from cashier.models import InvoiceNumber
    # TransactionExportNumber.reset_export_number(new_value=your_desired_value)
    @classmethod
    def reset_export_number(cls, new_value=0):
        counter, created = cls.objects.get_or_create(pk=1)
        counter.value = new_value
        counter.save()


class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    amount = models.FloatField(default=0)
    description = models.CharField(max_length=512)
    # Remove the auto_now_add=True argument
    time = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Get the current datetime
        current_datetime = datetime.now()

        # Format the datetime as a string
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

        # Set the formatted datetime as the value for the field
        self.time = formatted_datetime

        super().save(*args, **kwargs)

    def __str__(self):
        return ("%s ,%.2f, %s , %s, %s, %s" % (
        self.title, self.amount, self.time, self.description, self.owner, self.category))
