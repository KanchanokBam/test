from django.shortcuts import render
from .models import *
from django.views.generic import ListView

class CourseListView(ListView):
      model = Course
      template_name = 'list_course.html'
      context_object_name ='courses'

def course_idsearch(request):
      search = request.GET.get('code','')
      courses = Course.objects.filter(Course_id=search)
      return render (request, 'course_search.html', {'course' :courses})
# Create your views here.
