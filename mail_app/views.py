from django.shortcuts import render
from django.core.mail import send_mail


def reset_link_request(request):
    if request.method == 'POST':
        email = request.POST['email']
    else:
        return render(request, 'reset_link_request.html')


def reset_link_sent(request):
    return render(request, 'reset_link_sent.html')


def reset_password(request): 
    return render(request, 'reset_password.html')
   

def verification(request):
    return render(request, 'verification.html')


def activation(request):

    return redirect('chart')