from django.db import models


# Create your models here.
# from django.db import models


class InvoiceNumber(models.Model):
    value = models.IntegerField(default=0)

    @classmethod
    def get_next_invoice_number(cls):
        counter, created = cls.objects.get_or_create(pk=1)
        if not created:
            counter.value += 1
            counter.save()
        return counter.value

    # You can use this function in a python shell:
    # Start the virtual environment -> go to the main path
    # python manage.py shell
    # from cashier.models import InvoiceNumber
    # InvoiceNumber.reset_invoice_number(new_value=your_desired_value)
    @classmethod
    def reset_invoice_number(cls, new_value=0):
        counter, created = cls.objects.get_or_create(pk=1)
        counter.value = new_value
        counter.save()
