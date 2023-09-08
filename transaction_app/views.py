from django.shortcuts import render, redirect
from .models import Transaction
from category_app.models import Category

def add_transaction(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            entry = Transaction(
                amount = request.POST['amount'],
                category_id = request.POST['category'],
                user_id = request.user.id
            )
            entry.save()
            return redirect('add_transaction')
        else:
            # obtaining all categories
            categories = Category.objects.filter(user_id=request.user.id)
            ctx = { 'categories': categories }
            return render(request, 'add_transaction.html', ctx)
    else:
        return redirect('login_view')