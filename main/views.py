from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied        
import datetime
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render
from main.forms import SkillForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from main.models import Experience, Skill
def is_editor(user):
    return user.is_authenticated and user.groups.filter(name="Editor").exists()

def can_edit(user):
    # pemilik (superuser) atau Editor boleh mengubah data
    return user.is_superuser or is_editor(user)

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Aiko",
        "npm": "2506617140",
        "study_program": "S1 Sistem Informasi",
        "bio": (
        "Second year IS student at Universitas Indonesia."
        "Likes to learn new things."
        ),

        "last_login": last_login,
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Aiko",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_skill(request):
    skills = Skill.objects.all()

    for skill in skills:
        skill.star_count = skill.starred_by.count()
        skill.user_has_starred = (
            request.user.is_authenticated
            and skill.starred_by.filter(pk=request.user.pk).exists()
        )

    context = {
        "skill_list": skills,
        "can_edit": can_edit(request.user),
    }

    return render(request, "skill.html", context)

@login_required(login_url="/login/")  
def create_skill(request):
    if not request.user.is_superuser:
        raise PermissionDenied
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
    skills_json = serializers.serialize("json", skills, use_natural_foreign_keys=True)

    return HttpResponse(
        skills_json,
        content_type="application/json"
    )

@login_required(login_url="/login/")
def delete_skill(request, skill_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    skill = get_object_or_404(Skill, pk=skill_id)
    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")
        return redirect("main:show_skill")
    
    return redirect("main:show_skill")

@login_required(login_url="/login/")
def update_skill(request, skill_id):
    if not can_edit(request.user):
        raise PermissionDenied
    skill = get_object_or_404(Skill, pk=skill_id)
    form = SkillForm(request.POST or None, instance=skill)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill berhasil diperbarui!")
        return redirect("main:show_skill")

    context = {
        "name": "Aiko",
        "form": form,
        "skill": skill,
    }

    return render(request, "skill_form.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login")
        return redirect("main:login")

    context = {
        "name": "Aiko",
        "form": form,
    }

    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Aiko",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in skill.starred_by.all():
            skill.starred_by.remove(request.user)
        else:
            skill.starred_by.add(request.user)

    return redirect("main:show_skill")


