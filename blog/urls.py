from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),  # Example URL pattern for the blog app
    # Add more URL patterns for other views in the blog app as needed
]