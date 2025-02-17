"""learning_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='home'),
    path('account',include('contacts.urls')),
    url(r'^login/$', views.login_view ,name='login'),
    url(r'^logout/$', views.logout_view ,name='logout'),
    path('profile',views.profile,name='profile'),
    path("test",views.permissions_test),
    path('tracks',include('tracks.urls')),
    path('questions',include('questions.urls')),
    path('api/track',include('tracks.api.urls')),
    path('api/user',include('contacts.api.urls')),
    path('api/questions',include('questions.api.urls'))    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
