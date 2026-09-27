"""
URL configuration for workly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jobseeker import views

app_name="jobseeker"

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('saved_job/',views.saved_job,name='saved_job'),
    path('Save_job/<int:pk>/',views.Save_job,name='Save_job'),
    path('applye_jobs/',views.applye_jobs,name='applye_jobs'),
    path('applayed_jobs/',views.applayed_jobs,name='applayed_jobs'),
    path('delete_application/<int:pk>/',views.delete_application,name='delete_application'),
    path('resume_build/',views.resume_build,name='resume_build'),
    path('search/',views.search,name='search'),
    path('job_detail/',views.job_detail,name='job_detail'),
    path('all_feed/',views.all_feed,name='all_feed'),
    path('add_post/',views.add_post,name='add_post'),
    path('my_post/',views.my_post,name='my_post'),
    path('delete_post/<int:pk>/',views.delete_post,name='delete_post'),
    path('edit_post/<int:pk>/',views.edit_post,name='edit_post'),
    path('conection/',views.conection,name='conection'),
    path('messages/',views.messages,name='messages'),
    path('job_request/<int:pk>/',views.job_request,name='job_request'),
    path('job_accept/<int:pk>/',views.job_accept,name='job_accept'),
    path('setting/',views.setting,name='setting'),
    path('download-resume/',views.download_resume,name='download_resume'),

]