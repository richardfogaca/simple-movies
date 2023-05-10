from flask import redirect, url_for
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, expose
from dateutil import parser
from .models import Movie
from .utils import fetch_movie_data
from . import appbuilder

class MovieModelView(ModelView):
    datamodel = SQLAInterface(Movie)
    list_columns = ["title", "release_date"]
    route_base = "/movies"

    @expose("/load_data/")
    def load_data(self):
        if not self.appbuilder.get_session.query(Movie).count():
            data = fetch_movie_data()
            if data:
                for row in data['results']['bindings']:
                    movie_title = row['movieLabel']['value']
                    imdb_id = row['imdb_id']['value']
                    latest_publication_date_str = row['latest_publication_date']['value']
                    latest_publication_date = parser.parse(latest_publication_date_str).date()

                    movie = Movie(title=movie_title, release_date=latest_publication_date, imdb_id=imdb_id)
                    self.appbuilder.get_session.add(movie)

                self.appbuilder.get_session.commit()

        return redirect(url_for("MovieModelView.list"))
    
    @expose("/drop_data/")
    def drop_data(self):
        self.appbuilder.get_session.query(Movie).delete()
        self.appbuilder.get_session.commit()

        return redirect(url_for("MovieModelView.list"))

appbuilder.add_view(MovieModelView, "Movies", icon="fa-folder-open-o", category="Tables")
