from django.test import TestCase

from api.models import Book

class BookModelTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.book1 = Book.objects.create(
            title= 'purple hibiscus',
            author= 'chimamanda adichie ngozie',
            ISBN= '0007189885',
            published_date= '2003-10-30',
            book_copies= 5
        )

    def test_book_creation(self):
        self.assertTrue(Book.objects.get(title='Purple Hibiscus'))

    