from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('project/<int:project_id>/', views.view_project, name="project_detail"),
]