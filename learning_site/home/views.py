from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import TemplateView
from permissions.permissions import active_user_required
from django.contrib.auth import authenticate, login, logout
from tracks.models import exam_result
from questions.models import answer
from tracks.models import track
from contacts.models import profile as my_profile
from django.contrib import messages
# Create your views here.

def home_view (request):
    tracks = track.objects.all()[0:3]
    return render(request,'home/index.html',{"tracks":tracks})


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
            messages.error(request,"username or password are wrong")
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')

def profile (request):
    user = request.user
    profile_ = my_profile.objects.get(user=user)
    try :
        results = exam_result.objects.filter(user=user)
    except :
        results = None
    try :
        answers = answer.objects.filter(user=user)
        answers = len(answers)
    except:
        answers = 0
    return render (request,"profile/profile.html",{"user":user,"results":results,"answers":answers,"profile":profile_})
