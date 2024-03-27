import pytest
from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Фантастика")
        collector.set_book_genre("Что делать, если ваш кот хочет вас убить", "Детективы")
        assert collector.get_book_genre("Гордость и предубеждение и зомби") == "Фантастика" and collector.get_book_genre("Что делать, если ваш кот хочет вас убить") == "Детективы"

    def test_get_books_for_children_two_books(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Фантастика")
        collector.set_book_genre("Что делать, если ваш кот хочет вас убить", "Детективы")
        assert collector.get_books_for_children() != []

    def test_get_books_with_specific_genre_two_books(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Фантастика")
        collector.set_book_genre("Что делать, если ваш кот хочет вас убить", "Детективы")
        assert "Гордость и предубеждение и зомби" in collector.get_books_with_specific_genre("Фантастика")

    @pytest.mark.parametrize('name', ['Что делать, если ваш кот хочет вас убить', '1+1', 'Стрела'])
    def test_add_book_in_favorites_two_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    @pytest.mark.parametrize('name', ['Что делать, если ваш кот хочет вас убить', '1+1', 'Стрела'])
    def test_delete_book_from_favorites_two_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert collector.favorites == []

    def test_get_list_of_favorites_books_two_books(self):
        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        collector.add_book_in_favorites("Что делать, если ваш кот хочет вас убить")
        assert "Что делать, если ваш кот хочет вас убить" in collector.get_list_of_favorites_books()