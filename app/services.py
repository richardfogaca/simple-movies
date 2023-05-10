from typing import List, Tuple
from abc import ABC, abstractmethod
from .repositories import MovieRepository

class MovieService(ABC):
    @abstractmethod
    def get_movies(self) -> List[Tuple[str, str]]:
        pass

    @abstractmethod
    def store_movies(self, movies: List[Tuple[str, str]]) -> None:
        pass

class MovieServiceImpl(MovieService):
    def __init__(self, movie_repository: MovieRepository):
        self.movie_repository = movie_repository

    def get_movies(self) -> List[Tuple[str, str]]:
        return self.movie_repository.get_movies()

    def store_movies(self, movies: List[Tuple[str, str]]) -> None:
        self.movie_repository.store_movies(movies)
