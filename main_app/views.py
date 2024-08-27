from django.shortcuts import render

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def teacher_index(request):
    return render(request, 'teacher/index.html')