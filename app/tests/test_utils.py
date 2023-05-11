import pytest
from ..utils import WikiDataMovieService

def test_wiki_data_movie_service():
    wiki_data_service = WikiDataMovieService()
    movies = wiki_data_service.fetch_movies()
    assert isinstance(movies, list)
    if movies:
        movie_title, imdb_id, release_date = movies[0]
        assert isinstance(movie_title, str)
        assert isinstance(imdb_id, str)
        assert isinstance(release_date, str)
