from django.urls import path
from company import views

app_name = "company"

urlpatterns = [
    # Dashboard & Profile
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('jobs/', views.jobs, name='jobs'),
    path('create_jobs/', views.create_jobs, name='create_jobs'),
    path('applications/', views.applications, name='applications'),
    path('applicant/', views.applicant, name='applicant'),
    path('sta_tus/', views.sta_tus, name='sta_tus'),
]
