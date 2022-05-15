from django.test import TestCase
from .models import Student,School,Book
# Create your tests here.

class studentData(TestCase):
    def setUp(self) -> None:
        school = School.objects.create(
            name="Menihek High School",
            phone_number="+9167555896",
            is_active=True
        )
        book = Book.objects.create(
            name = "Basic Instinct",
            is_active = True
        )
        Student.objects.create(
            first_name = "Dominik",
            last_name = "lol",
            email = "dbarricki@amazon.com",
            gender = "M",
            school = school,
            book = book,
            pages_read_count = "269"
        )
    def test_insert(self):
        """database test"""
        student = Student.objects.get(first_name= "Dominik")
        self.assertEqual(student.first_name,"Dominik")