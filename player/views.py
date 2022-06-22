from django.shortcuts import render


def home(request) -> render:
    """Главная страница."""
    return render(request, "index.html")