import openpyxl as openpyxl
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import ListView
from Inventory.models import Transaction, Item, Client
from datetime import datetime, timedelta

# I am not sure I imported Transaction properly


from django.db.models import Q
from datetime import datetime

from django.shortcuts import render
from django.utils import timezone

from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import csv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from Inventory.models import Transaction, Item, Client
from datetime import datetime, timedelta
import csv
from .models import Expense
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter
from cashier.views import receipt
from datetime import date

@login_required
def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-trans_id')
    items = Item.objects.all()
    clients = Client.objects.all()
    users = User.objects.all()
    types = Transaction.objects.values_list('type', flat=True).distinct()

    if request.method == 'GET':
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')
        item = request.GET.get('item')
        client_name = request.GET.get('client')
        user = request.GET.get('user')
        type = request.GET.get('type')

        if from_date and to_date:
            to_date = datetime.strptime(to_date, '%Y-%m-%d') + timedelta(days=1)
            transactions = Transaction.objects.filter(time__range=(from_date, to_date))

        if item:
            transactions = transactions.filter(item=item)

        if client_name:
            client = get_object_or_404(Client, name=client_name)
            transactions = transactions.filter(client=client)

        if user:
            transactions = transactions.filter(user=user)

        if type:
            transactions = transactions.filter(type=type)

        # Check if the "export" parameter is in the request
        if 'export' in request.GET:
            receipt(transactions)

    return render(request, 'transaction_list.html',
                  {'items': items, 'clients': clients, 'users': users, 'types': types, 'transactions': transactions})

@login_required
def balance_sheet(request):
    items = Item.objects.all()
    if request.method == 'GET':
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')

        cash = 0
        profit = 0
        inventory_purchase_cost = 0
        shipping_cost = 0
        internal_expenses = 0
        net_profit = 0
        discounts = 0
        asset_value = 0
        transactions_count = 0
        quantity_sold = 0
        items_sold = {}

        for item in items:
            inventory_purchase_cost += (item.purchase_cost * int(item.quantity))
            asset_value += ((item.purchase_cost + item.shipping_cost) * int(item.quantity))

        if from_date and to_date:
            to_date = datetime.strptime(to_date, '%Y-%m-%d') + timedelta(days=1)
            transactions = Transaction.objects.filter(time__range=(from_date, to_date))
            expenses = Expense.objects.filter(time__range=(from_date, to_date))

            if transactions:
                for transaction in transactions:
                    if transaction.type == "transfer" or transaction.type == "wholesale":
                        cash += transaction.selling_price * transaction.quantity
                        transactions_count += 1
                        quantity_sold += transaction.quantity
                        shipping_cost += transaction.item.shipping_cost * int(transaction.quantity)
                        if transaction.item in items_sold:
                            items_sold[transaction.item] += transaction.quantity
                        else:
                            items_sold[transaction.item] = transaction.quantity

                    elif transaction.type == "return":
                        cash -= transaction.selling_price * transaction.quantity
                        transactions_count -= 1
                        quantity_sold -= transaction.quantity
                        if transaction.item in items_sold:
                            items_sold[transaction.item] -= transaction.quantity
                        else:
                            items_sold[transaction.item] = -transaction.quantity

                    profit += transaction.profit
                    discounts += transaction.discount

            if expenses:
                for expense in expenses:
                    internal_expenses += expense.amount

            net_profit = profit - internal_expenses

        context = {
            'cash': round(cash,2),
            'profit': round(profit,2),
            'inventory_purchase_cost': round(inventory_purchase_cost,2),
            'shipping_cost': round(shipping_cost,2),
            'internal_expenses': round(internal_expenses,2),
            'net_profit': round(net_profit,2),
            'discounts': round(discounts,2),
            'asset_value': round(asset_value,2),
            'transactions_count': round(transactions_count,2),
            'quantity_sold': round(quantity_sold,2),
            'items_sold': items_sold,
            'from_date': request.GET.get('from_date', ''),
            'to_date': request.GET.get('to_date', ''),
            'today': date.today().isoformat(),
        }

    return render(request, 'balance_sheet.html', context)


@login_required
def financials(request):
    return render(request, 'finance_page.html')
