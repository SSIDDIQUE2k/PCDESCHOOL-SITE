
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.utils import timezone
from datetime import timedelta

from .models import Teacher, Event # Import the Teacher model

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

def home(request):
    today = timezone.now()
    start_date = today - timedelta(days=today.day-1)  # Start of the month
    end_date = start_date + timedelta(days=31)  # End date for 31 days

    events = Event.objects.filter(start_time__range=(start_date, end_date))

    return render(request, 'home.html', {'events': events, 'today': today})

def contact(request):
    return render(request, 'contact.html')


def teacher_index(request):
    teachers = Teacher.objects.all()  # look familiar?
    return render(request, 'teachers/index.html', {'teachers': teachers})


def teacher_detail(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    return render(request, 'teachers/detail.html', {'teacher': teacher})

# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#         # This is how to create a 'user' form object
#         # that includes the data from the browser
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             # This will add the user to the database
#             user = form.save()
#             # This is how we log a user in
#             login(request, user)
#             return redirect('home')
#         else:
#             error_message = 'Invalid sign up - try again'
#     # A bad POST or a GET request, so render signup.html with an empty form
#     form = UserCreationForm()
#     context = {'form': form, 'error_message': error_message}
#     return render(request, 'signup.html', context)
#     # Same as: 
#     # return render(
#     #     request, 
#     #     'signup.html',
#     #     {'form': form, 'error_message': error_message}
#     # )

def mission_statement(request):
    return render(request, 'about_directories/statement.html')

def belief(request):
    return render(request, 'about_directories/belief.html')

def policy(request):
    return render(request, 'academics_directories/academic-policy.html')

def Tution(request):
    return render(request, 'academics_directories/tution.html')

def DayCare(request):
    return render(request, 'academics_directories/dayCare.html')

def Academics(request):
    return render(request, 'academics_directories/academics.html')

def Conduct(request):
    return render(request, 'academics_directories/conduct.html')

def attendance(request):
    return render(request, 'academics_directories/attendance.html')

def a_d_Procedures(request):
    return render(request, 'spg_directories/a_d_procedures.html')

def Health_Issues(request):
    return render(request, 'spg_directories/health-issues.html')

def attire_requirement(request):
    return render(request, 'spg_directories/attire_requirement.html')

def Gym(request):
    return render(request, 'spg_directories/gym.html')

def Electronics(request):
    return render(request, 'spg_directories/electronics.html')

def Trips(request):
    return render(request, 'spg_directories/trips.html')






