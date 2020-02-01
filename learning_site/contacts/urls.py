from django.urls import path
from .views import create_user,activate,forgot_password_mail,reset_password,change_password,teacher_details
from django.conf.urls import url

app_name = 'contacts'

urlpatterns = [
   path('/signup',create_user,name='signup'),
   url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
       activate, name='activate'),
    path('/resetmail',forgot_password_mail,name='resetmail'),
    url(r'^resetmail/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        reset_password, name='reset'),
    path('/changepassword',change_password,name='change_password'),
    path('/teacher/<int:pk>',teacher_details,name="teacher"),
]