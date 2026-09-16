from django.forms import ModelForm, TextInput
from main.models import Skill


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ["name", "category", "level"]
        labels = {
            "name": "Nama Skill",
            "category": "Kategori",
            "level": "Level",
        }
        widgets = {
            "name": TextInput(attrs={"placeholder": "Problem Solving"}),
            "category": TextInput(attrs={"placeholder": "Soft Skill"}),
            "level": TextInput(attrs={"placeholder": "-"}),
        }