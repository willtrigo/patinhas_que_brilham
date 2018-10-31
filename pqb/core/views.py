"""Views of app core."""
from django.shortcuts import render


def view_home(request):
    """Create view home."""
    return render(request, 'core/home.html')
