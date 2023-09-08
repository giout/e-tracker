from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('chart')
    else: 
        return redirect('login_view')