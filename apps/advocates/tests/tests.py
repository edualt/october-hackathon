from apps.advocates.models import Advocate
from apps.companies.models import Company
from django.test import TestCase


class AdvocateTest(TestCase):
    def setUp(self):
        Company.objects.create(
            name="agora",
            summary="summary"
        ),
        Advocate.objects.create(
            name="edualt",
            short_bio="shorttt",
            long_bio="longgg",
            years_of_experience=1,
            company=Company.objects.get(name="agora")
        )

    def test_create_advocate(self):
        advocate = Advocate.objects.get(name="edualt")
        self.assertEqual(advocate.name, "edualt")
        self.assertEqual(advocate.short_bio, "shorttt")
        self.assertEqual(advocate.long_bio, "longgg")
        self.assertEqual(advocate.years_of_experience, 1)
        self.assertEqual(advocate.company.name, "agora")
