from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Item, Transaction, Client
from django.shortcuts import render, get_object_or_404
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Item
from .forms import ItemForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from .models import Item
from .forms import ItemForm

@login_required
def home(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'home.html', {'items': items})


@login_required
def item_list(request):
    items = Item.objects.all().order_by('-item_id')
    return render(request, 'item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('Inventory:item_list')
    else:
        form = ItemForm()
    return render(request, 'item_create.html', {'form': form})

def item_edit(request, item_id):
    item = get_object_or_404(Item, item_id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('Inventory:item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_edit.html', {'form': form})

def item_delete(request, item_id):
    item = get_object_or_404(Item, item_id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('Inventory:item_list')
    return render(request, 'Inventory/item_delete.html', {'item': item})
@login_required
def rebuy_list(request):
    items = Item.objects.all()
    return render(request, 'rebuy_list.html', {'items': items})

@login_required
def item_details(request, item_id):
    discount=0
    type="NULL"
    item = get_object_or_404(Item, pk=item_id)
    clients = Client.objects.all()
    context = {'item': item, 'clients': clients}
    if request.method == 'POST':
        quantity = request.POST['quantity']
        client = request.POST['client']
        selling_price = request.POST['selling_price'] # get the selling_price value from POST request
        if 'transfer' in request.POST:
            transaction_type = Transaction.TYPE_CHOICES[0][0]
            type='transfer'
            item.quantity -= int(quantity)
            item.save()
            discount= item.selling_price - request.POST['selling_price']
        elif 'return' in request.POST:
            transaction_type = Transaction.TYPE_CHOICES[1][0]
            type = 'return'
            item.quantity += int(quantity)
            item.save()
            discount =  request.POST['selling_price'] - item.selling_price
        transaction = Transaction.objects.create(
            item=item,
            client=client,
            quantity=int(quantity),
            transaction_type=transaction_type,
            selling_price=float(selling_price) * int(quantity), # save the selling_price value in the Transaction model
            discount= discount * int(quantity),
            type=type,
            TVA = round(float(selling_price) * 0.11 * int(quantity), 2)
        )
        transaction.save()
        return redirect('item_details', context)
    return render(request, 'details.html', context)


@login_required
def transferitm(request, item_id):
    client = Client.objects.get(name=request.POST.get("client"))
    type = 'transfer'
    item = Item.objects.get(pk=item_id)
    quantity = request.POST.get("quantity")
    #selling_price = request.POST.get("selling_price")
    selling_price = request.POST.get("selling_price")
    user = request.user.username
    discount = ((item.selling_price ) - float(request.POST['selling_price'])) * int(quantity)
    profit = ((item.selling_price - item.purchase_cost - item.shipping_cost) * int(quantity))-discount
    TVA= round(float(request.POST['selling_price']) * 0.11 * int(quantity) , 2)
    transaction = Transaction(quantity=quantity, item=item, client=client, selling_price=selling_price, user=user, discount=discount,type=type, profit=profit,TVA=TVA)
    transaction.save()
    item.quantity = item.quantity - int(quantity)
    item.save()
    return render(request, 'transferitm.html',
                  {'transaction': transaction, 'quantity': quantity, 'item': item, 'Selling Price': selling_price,
                   user: 'User', client: 'client',TVA:'TVA'})

@login_required
def returnitm(request, item_id):
    client = Client.objects.get(name=request.POST.get("client"))
    type = 'return'
    item = Item.objects.get(pk=item_id)
    quantity = request.POST.get("quantity")
    selling_price = request.POST.get("selling_price")
    user = request.user.username
    discount = (float(request.POST['selling_price']) - item.selling_price) * int(quantity)
    profit = ((item.shipping_cost + item.purchase_cost - item.selling_price) * int(quantity)) - discount

    transaction = Transaction(quantity=quantity, item=item, client=client, selling_price=selling_price, user=user, discount=discount, type=type, profit=profit)
    transaction.save()
    item.quantity = item.quantity + int(quantity)
    item.save()
    return render(request, 'returnitm.html',
                  {'transaction': transaction, 'quantity': quantity, 'item': item, 'Selling Price': selling_price,
                   user: 'User', client: 'client'})

