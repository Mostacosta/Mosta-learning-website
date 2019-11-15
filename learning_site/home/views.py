from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import TemplateView
from permissions.permissions import active_user_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home_view (request):
    return render(request,'home/index.html')


@active_user_required
def permissions_test (request):
    return HttpResponse("fsksdmfkmdsl")

def login_view(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            # Redirect to a success page.
            return redirect('home')
            ...
        else:
            # Return an 'invalid login' error message.
           ...
    return render(request,'contacts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')