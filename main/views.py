from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render
from main.forms import SkillForm
from django.shortcuts import get_object_or_404

from main.models import Experience, Skill
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

def show_skill(request):
    json_response = get_skills_json(request)

    skills = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    skills = [skill.object for skill in skills]

    context = {
        "skill_list": skills,
    }

    return render(request, "skill.html", context)

def create_skill(request):
    form = SkillForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill baru berhasil ditambahkan!")
        return redirect("main:show_skill")
    context = {
        "name": "Aiko",
        "form": form,
        }
    return render(request, "skill_form.html", context)

def get_skills_json(request):
    skills = Skill.objects.all()
    skills_json = serializers.serialize("json", skills)

    return HttpResponse(
        skills_json,
        content_type="application/json"
    )

def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")
        return redirect("main:show_skill")
    
    return redirect("main:show_skill")


