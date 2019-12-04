from django.urls import path,include
from .views import user_api
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

urlpatterns = [
    path("",user_api.as_view(),name="user_api"),
    path("obtainjwt",obtain_jwt_token,name="obtain_jwt"),
    path("refreshjwt",refresh_jwt_token,name="refresh_jwt")

]