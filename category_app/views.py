from django.shortcuts import render, redirect
from .models import Category

def add_category(request):
    if request.method == 'POST':  
        entry = Category(
            description = request.POST['description'] 
        )
        entry.save()
        return redirect('add_category')
    else:
        return render(request, 'add_category.html')