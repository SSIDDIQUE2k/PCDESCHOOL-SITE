from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teachers/', views.teacher_index, name='teacher-index'),
    path('teachers/<int:teacher_id>/', views.teacher_detail, name='teacher-detail'),
]
