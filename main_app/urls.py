from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('login/', views.Login.as_view(), name='sign-in'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('teachers/', views.teacher_index, name='teacher-index'),
    path('teachers/<int:teacher_id>/', views.teacher_detail, name='teacher-detail'),
    path('teachers/create/', views.TeacherCreate.as_view(), name='teacher-create'),
    path('teachers/<int:pk>/update/', views.TeacherUpdate.as_view(), name='teacher-update'),
    path('teachers/<int:pk>/delete/', views.TeacherDelete.as_view(), name='teacher-delete'),
    path('accounts/signup/', views.signup, name='sign-up'),

    
    
]
