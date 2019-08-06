from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from permissions.permissions import active_user_required
# Create your views here.

def home_view (request):
    return render(request,'home/homepage.html',{'user':request.user.username})

@active_user_required
def permissions_test (request):
    return HttpResponse("fsksdmfkmdsl")
