# microsvc/urls.py
from django.urls import path
from . import views
from .views import PredictionAPI # <-- Import the API class

app_name = 'microsvc'
urlpatterns = [
    # 1. HTML Demo Page
    path("demo/", views.api_demo, name="api_demo"),
    
    # 2. API Endpoint for POST requests
    path("predict/", PredictionAPI.as_view(), name="predict_api"), # <-- NEW API PATH
]