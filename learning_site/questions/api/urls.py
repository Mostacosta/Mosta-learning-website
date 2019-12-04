from django.urls import path
from questions.api.views import questions_views


urlpatterns = [
    path("",questions_views.as_view())

]