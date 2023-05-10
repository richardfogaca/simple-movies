from typing import List, Tuple
from abc import ABC, abstractmethod
from .models import Movie

class MovieRepository(ABC):
    @abstractmethod
    def get_movies(self) -> List[Movie]:
        pass

    @abstractmethod
    def store_movies(self, movies: List[Tuple[str, str]]) -> None:
        pass


class SQLAlchemyMovieRepository(MovieRepository):
    def __init__(self, session):
        self.session = session

    def get_movies(self) -> List[Movie]:
        return self.session.query(Movie).all()

    def store_movies(self, movies: List[Tuple[str, str]]) -> None:
        for movie in movies:
            self.session.add(movie)
        self.session.commit()
