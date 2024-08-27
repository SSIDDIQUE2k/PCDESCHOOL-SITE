from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Teacher  # Import the Teacher model

class Login(LoginView):
    template_name = 'login.html'



class TeacherCreate(CreateView):
    model = Teacher
    fields = '__all__'

class TeacherUpdate(UpdateView):
    model = Teacher
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = '__all__'

class TeacherDelete(DeleteView):
    model = Teacher
    success_url = '/teachers/'



# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def teacher_index(request):
    teachers = Teacher.objects.all()  # look familiar?
    return render(request, 'teachers/index.html', {'teachers': teachers})

def teacher_detail(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    return render(request, 'teachers/detail.html', {'teacher': teacher})







