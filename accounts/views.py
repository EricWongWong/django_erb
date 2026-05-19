from django.shortcuts import render, redirect
from . import views

app_name = 'accounts'

# Create your views here.
def register(request):
    if request.method == "POST":
        first_nme = request.POST['first_name']
        last_nme = request.POST['last_name']      
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2= request.POST['password2']
        return redirect(request, "accounts/register.html")
    else: 
        return render(request, "accounts/register.html")

def login(request):
    return render(request, "accounts/login.html")

def logout(request):
    return render(request, "accounts/logout.html")

