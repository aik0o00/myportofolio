from django.urls import path
from main.views import show_main, show_experience, show_skill, create_skill, get_skills_json, delete_skill, update_skill, register, login_user, logout_user, toggle_star, create_skill_ajax, create_experience, update_experience, delete_experience, toggle_star_experience, get_experiences_json

app_name = "main"
urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/update/", update_experience, name="update_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("experience/<uuid:experience_id>/star/", toggle_star_experience, name="toggle_star_experience"),
    path("skill/", show_skill, name="show_skill"),
    path("skill/add/", create_skill, name="create_skill"),
    path("skill/json/", get_skills_json, name="get_skills_json"),
    path("skill/<uuid:skill_id>/delete/", delete_skill, name="delete_skill"),
    path("skill/<uuid:skill_id>/update/", update_skill, name="update_skill"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("skill/<uuid:skill_id>/star/", toggle_star, name="toggle_star"),
    path("skill/add-ajax/", create_skill_ajax, name="create_skill_ajax"),
    path("experience/json/", get_experiences_json, name="get_experiences_json"),
    ]
