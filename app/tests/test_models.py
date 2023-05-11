import pytest
from ..models import Movie

def test_movie_model():
    movie = Movie(title="Test Movie", imdb_id="tt1234567")
    assert movie.title == "Test Movie"
    assert movie.imdb_id == "tt1234567"
