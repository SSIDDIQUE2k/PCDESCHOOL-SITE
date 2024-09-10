from django.urls import path
from . import views # Import views to connect routes to view functions

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.Login.as_view(), name='sign-in'),
    path('', views.home, name='home'),
    path('about_directories/statement/', views.mission_statement, name='mission-statement'),
    path('about_directories/belief/', views.belief, name='belief'),
    path('contact/', views.contact, name='contact'),
    path('teachers/', views.teacher_index, name='teacher-index'),
    path('teachers/<int:teacher_id>/', views.teacher_detail, name='teacher-detail'),
    path('teachers/create/', views.TeacherCreate.as_view(), name='teacher-create'),
    path('teachers/<int:pk>/update/', views.TeacherUpdate.as_view(), name='teacher-update'),
    path('teachers/<int:pk>/delete/', views.TeacherDelete.as_view(), name='teacher-delete'),
    path('academics_directories/academic-policy', views.policy, name='academic-policy'),
    path('academics_directories/tution', views.Tution, name='tution'),
    path('academics_directories/dayCare', views.DayCare, name='dayCare'),
    path('academics_directories/academics', views.Academics, name='academics'),
    path('academics_directories/conduct', views.Conduct, name='conduct'),
    path('academics_directories/attendance', views.attendance, name='attendance'),
    path('spg_directories/a-d_procedures', views.a_d_Procedures, name='a-d_procedures'),
    path('spg_directories/health-issues', views.Health_Issues, name='health-issues'),
    path('spg_directories/attire_requirement', views.attire_requirement, name='attire_requirement'),
    path('spg_directories/gym', views.Gym, name='gym'),
    path('spg_directories/electronics', views.Electronics, name='electronics'),
       path('spg_directories/trips', views.Trips, name='trips'),
       
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
