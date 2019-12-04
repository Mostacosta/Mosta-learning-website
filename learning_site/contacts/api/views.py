from ..models import profile
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import profile_serializer,user_serializer
from rest_framework.views import APIView

class user_api (APIView):
    def get(self, request,format=None):
        q = request.GET.get("q", None)
        if q:
            username = q
            user = User.objects.get(username = username)
            profile_ = profile.objects.get(user = user)
            serializer = profile_serializer(profile_)
            return Response (serializer.data)
        return Response("mfesh 7aga b3tha")
    def post (self,request,format=None):
        data = request.data
        profile_ = profile_serializer(data=data)
        user = user_serializer(data=data)
        if profile_.is_valid() and user.is_valid():
            user=user.save()
            profile_.save(user=user)
            return Response(profile_.data)
        return Response(user.errors)

        
    





        
    