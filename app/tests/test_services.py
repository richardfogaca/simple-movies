import pytest
from ..services import MovieService

def test_movie_service_interface():
    with pytest.raises(TypeError):
        service = MovieService()
