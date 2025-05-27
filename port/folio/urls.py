# folio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',views.admin, name='admin'),
    path('',views.home, name='home'),
    path('projects/',views.projects, name='projects'),
    #path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('contact/',views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
]
