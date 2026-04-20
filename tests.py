import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Шерлок Холмс')

        assert collector.get_books_genre() == {
            'Дюна': '',
            'Шерлок Холмс': ''
        }

    @pytest.mark.parametrize('name', ['', 'А' * 41])
    def test_add_new_book_not_add_invalid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert collector.get_books_genre() == {}

    def test_add_new_book_not_add_duplicate_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')

        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_sets_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_book_genre_returns_empty_string_for_new_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')

        assert collector.get_book_genre('Дюна') == ''

    def test_get_books_with_specific_genre_returns_books_list(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']

    @pytest.mark.parametrize(
        'name, genre, expected',
        [
            ('Дюна', 'Фантастика', True),
            ('Оно', 'Ужасы', False),
            ('Шерлок Холмс', 'Детективы', False),
            ('Ну, погоди!', 'Мультфильмы', True),
            ('Маска', 'Комедии', True),
        ]
    )
    def test_get_books_for_children_returns_only_books_without_age_rating(
        self, name, genre, expected
    ):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        books_for_children = collector.get_books_for_children()

        if expected:
            assert name in books_for_children
        else:
            assert name not in books_for_children

    def test_add_book_in_favorites_adds_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_add_book_in_favorites_not_add_duplicate_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_delete_book_from_favorites_removes_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == []