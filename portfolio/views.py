# portfolio/views.py
from django.shortcuts import render

def index(request):
    """Renders the main portfolio home page."""
    # Context dictionary to pass dynamic data to the template
    context = {
        "name": "Eddy Montana", # Use your actual name here
        "title_tag": "AI/ML Engineer & Full-Stack Developer",
        "summary": "Leveraging Django, Python, and JavaScript to build scalable applications and integrate custom AI models."
    }
    # Renders the index.html template from the portfolio/templates/ directory
    return render(request, "portfolio/index.html", context)
