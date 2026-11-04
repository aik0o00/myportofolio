
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from main.models import Experience, Skill

class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
        title="Mahasiswa PBP",
        description="Belajar dan memahami pengembangan web.",
        category="part-time",
    )
    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response,
        f'href="{reverse("main:show_experience")}"'
        )

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Mahasiswa PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, 'id="loading"')
        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"'
        )

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="empty"')

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()

        self.assertFalse(self.experience.is_ongoing)

class SkillTest(TestCase):
     def setUp(self):
            self.skill = Skill.objects.create(
            name="Problem Solving",
            category="Soft Skill",
            level="-",
        )
     def test_skill_url_is_accessible(self):
        response = self.client.get(reverse("main:show_skill"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")

     def test_skill_data_appears(self):
        response = self.client.get(reverse("main:show_skill"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, 'id="loading"')

     def test_empty_skill_page(self):
        Skill.objects.all().delete()
        response = self.client.get(reverse("main:show_skill"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="empty"')





