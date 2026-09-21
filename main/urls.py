from django.urls import path
from main.views import show_main, show_experience, show_skill, create_skill, get_skills_json, delete_skill, update_skill

app_name = "main"
urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("skill/", show_skill, name="show_skill"),
    path("skill/add/", create_skill, name="create_skill"),
    path("skill/json/", get_skills_json, name="get_skills_json"),
    path("skill/<int:skill_id>/delete/", delete_skill, name="delete_skill"),
    path("skill/<int:skill_id>/update/", update_skill, name="update_skill"),
]
