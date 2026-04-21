import pytest

class TestBooksCollector:

    def test_add_new_book_adds_book_to_books_genre(self, collector):
        collector.add_new_book('Дюна')

        assert collector.books_genre == {'Дюна': ''}

    @pytest.mark.parametrize('name', ['', 'А' * 41])
    def test_add_new_book_not_add_invalid_name(self, collector, name):
        collector.add_new_book(name)

        assert collector.books_genre == {}

    def test_add_new_book_not_add_duplicate_book(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')

        assert len(collector.books_genre) == 1

    def test_set_book_genre_sets_genre_for_added_book(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.books_genre['Дюна'] == 'Фантастика'

    def test_get_book_genre_returns_genre_by_name(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_books_with_specific_genre_returns_books_with_given_genre(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']

    def test_get_books_genre_returns_current_books_genre_dict(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')

        assert collector.get_books_genre() == {
            'Дюна': '',
            'Оно': ''
        }

    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Дюна', 'Фантастика'),
            ('Ну, погоди!', 'Мультфильмы'),
            ('Маска', 'Комедии'),
        ]
    )
    def test_get_books_for_children_returns_books_without_age_rating(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name in collector.get_books_for_children()

    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Оно', 'Ужасы'),
            ('Шерлок Холмс', 'Детективы'),
        ]
    )
    def test_get_books_for_children_not_returns_books_with_age_rating(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name not in collector.get_books_for_children()

    def test_add_book_in_favorites_adds_book_to_favorites(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_delete_book_from_favorites_deletes_book_from_favorites(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == []