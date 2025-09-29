# aiprofolio/urls.py

from django.contrib import admin
from django.urls import path, include # <-- Import include

urlpatterns = [
    # Admin is the first entry
    path('admin/', admin.site.urls),

    # Traffic for the main portfolio pages
    path('', include('portfolio.urls')), # Direct the root to the portfolio app

    # Traffic for the microservice API demo
    path('api/', include('microsvc.urls')), # Prefix API routes with /api/
]