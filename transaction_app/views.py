from django.shortcuts import render, redirect
from .models import Transaction
from category_app.models import Category

def add_transaction(request):
    if request.method == 'POST':
        entry = Transaction(
            amount = request.POST['amount'],
            category_id = request.POST['category']
        )
        entry.save()
        return redirect('add_transaction')
    else:
        # obtaining all categories
        categories = Category.objects.all()
        ctx = { 'categories': categories }
        return render(request, 'add_transaction.html', ctx)