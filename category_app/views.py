from django.shortcuts import render, redirect
from .models import Category

def add_category(request):
    if request.user.is_authenticated: 
        if request.method == 'POST':  
            entry = Category(
                description = request.POST['description'],
                user_id = request.user.id
            )
            entry.save()
            return redirect('add_category')
        else:
            return render(request, 'add_category.html')
    else:
        return redirect('login_view')