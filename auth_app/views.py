from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_view(request):
    ctx = {}
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticating
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_transaction')

        else: 
            ctx = {'error_auth': True}

    return render(request, 'login.html', ctx)


def signup_view(request): 
    ctx = {}

    if request.method == 'POST':
        username = request.POST['username'] 
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        # password verification
        if password == confirm_password:
            # user registration
            user = User.objects.create_user(username, email, password)
            user.save()
            login(request, user)
            return redirect('add_transaction')
        
        # if passwords don't match
        else: 
            ctx = {'error_pass_match': True}
    
    return render(request, 'signup.html', ctx)


def logout_view(request):  
    logout(request)
    return redirect('signup_view')