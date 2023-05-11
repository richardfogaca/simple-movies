import pytest
from ..views import MovieModelView

def test_movie_model_view():
    movie_view = MovieModelView()
    assert movie_view.list_columns == ["title", "release_date"]
    assert movie_view.route_base == "/movies"
