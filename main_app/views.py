from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .models import Teacher  # Import the Teacher model

class Login(LoginView):
    template_name = 'login.html'



class TeacherCreate(LoginRequiredMixin,CreateView):
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

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )









