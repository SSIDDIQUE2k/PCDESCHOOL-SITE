from django.shortcuts import render
from .models import Teacher


# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def teacher_index(request):
    teachers = Teacher.objects.all()  # look familiar?
    return render(request, 'teachers/index.html', {'teachers': teachers})