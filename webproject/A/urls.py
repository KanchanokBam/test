
from django.urls import path, include
from .views import *
from django.urls import path

urlpatterns = [

     path('course/', CourseListView.as_view(),name='course_list'),
     path('id_search', course_idsearch, name= 'search_id')

]