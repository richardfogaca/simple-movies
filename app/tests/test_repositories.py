import pytest
from ..models import Movie
from ..repositories import MovieRepository

def test_movie_repository_interface():
    with pytest.raises(TypeError):
        repo = MovieRepository()
