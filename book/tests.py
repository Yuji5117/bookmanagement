from django.test import TestCase
from django.urls import reverse
from .models import Book, Category


class BookModelTests(TestCase):
    def test_is_empty(self):
        saved_books = Book.objects.all()
        self.assertEqual(saved_books.count(), 0)




class BookIndexTests(TestCase):
    def test_get(self):
        response = self.client.get(reverse('book:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['book_list'], [])


    def test_1book_and_get(self):
        category_name = Category.objects.create(name_category='food') 
        book = Book.objects.create(auther='yuji', title='thanks', category=category_name, comment='very nice')
        response = self.client.get(reverse('book:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['book_list'], ['<book: thanks>'], ['<book: category_name>'])
        self.assertContains(response, book.title)




    def test_2book_and_get(self):
        category_name = Category.objects.create(name_category='food') 
        book = Book.objects.create(auther='yuji', title='thanks', category=category_name, comment='very nice')
        book2 = Book.objects.create(auther='dahey', title='cool', comment='very cool')
        response = self.client.get(reverse('book:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['book_list'], ['<book: thanks>', '<book: cool>'], ordered=False)
        self.assertContains(response, book.title)
        self.assertContains(response, book2.title)
