from django.shortcuts import render

def add_transaction(request):
    return render(request, 'add_transaction.html')