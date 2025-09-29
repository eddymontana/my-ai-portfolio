# portfolio/urls.py
from django.urls import path
from . import views

# Naming the app space is a best practice for reverse URL lookup
app_name = 'portfolio' 
urlpatterns = [
    # The empty string "" path maps to the site root (e.g., http://127.0.0.1:8000/)
    path("", views.index, name="index"),
]