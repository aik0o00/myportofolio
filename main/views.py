from django.shortcuts import render

from main.models import Experience
def show_main(request):
    context = {
        "name": "Aiko",
        "npm": "2506617140",
        "study_program": "S1 Sistem Informasi",
        "bio": (
        "Second year IS student at Universitas Indonesia."
        "Likes to learn new things."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Aiko",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

