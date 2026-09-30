from django import forms
from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from main.models import Skill


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ["name", "category", "level", "description"]

        labels = {
            "name": "Nama Skill",
            "category": "Kategori",
            "level": "Level",
            "description": "Deskripsi",
        }

        widgets = {
            "name": TextInput(
                attrs={"placeholder": "Problem Solving"}
            ),
            "category": TextInput(
                attrs={"placeholder": "Soft Skill"}
            ),
            "level": TextInput(
                attrs={"placeholder": "-"}
            ),
        }

    def clean_name(self):
        name = strip_tags(self.cleaned_data["name"]).strip()

        if not name:
            raise ValidationError(
                "Nama skill tidak boleh hanya berisi tag HTML."
            )

        return name

    def clean_category(self):
        return strip_tags(
            self.cleaned_data["category"]
        ).strip()

    def clean_level(self):
        return strip_tags(
            self.cleaned_data["level"]
        ).strip()

    def clean_description(self):
        return strip_tags(
            self.cleaned_data["description"]
        ).strip()