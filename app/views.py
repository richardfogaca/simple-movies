from flask import redirect, url_for
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, expose
from .models import Movie
from .repositories import SQLAlchemyMovieRepository
from .services import MovieServiceImpl
from .utils import WikiDataMovieService
from . import appbuilder

class MovieModelView(ModelView):
    datamodel = SQLAInterface(Movie)
    list_columns = ["title", "release_date"]
    route_base = "/movies"

    @expose("/load_data/")
    def load_data(self):
        movie_repo = SQLAlchemyMovieRepository(appbuilder.get_session)
        movie_service = MovieServiceImpl(movie_repo)
        if not movie_service.get_movies():
            wiki_data_movie_service = WikiDataMovieService()
            data = wiki_data_movie_service.fetch_movies()
            if data:
                movies = []
                for row in data:
                    movie_title, imdb_id = row
                    movie = Movie(title=movie_title, imdb_id=imdb_id)
                    movies.append(movie)

                movie_service.store_movies(movies)

        return redirect(url_for("MovieModelView.list"))

    @expose("/drop_data/")
    def drop_data(self):
        movie_repo = SQLAlchemyMovieRepository(appbuilder.get_session)
        movie_service = MovieServiceImpl(movie_repo)
        for movie in movie_service.get_movies():
            appbuilder.get_session.delete(movie)
        appbuilder.get_session.commit()

        return redirect(url_for("MovieModelView.list"))

appbuilder.add_view(MovieModelView, "Movies", icon="fa-folder-open-o", category="Tables")
