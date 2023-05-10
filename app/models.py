from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Date

class Movie(Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    release_date = Column(Date, nullable=True)
    imdb_id = Column(String(16), nullable=False, unique=True)

    def __repr__(self):
        return f"<Movie {self.title} ({self.release_date})>"
