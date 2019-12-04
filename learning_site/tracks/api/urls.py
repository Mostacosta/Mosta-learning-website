from django.urls import path,include
from tracks.api.views import all_list,exam_api

urlpatterns = [
    path('/all/<str:which>',all_list.as_view(),name='lesson_list'),
    path('/exam/<str:course_name>',exam_api.as_view(),name='exam_api')

]