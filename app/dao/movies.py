
from app.dao.models.movies import Movies, MoviesSchema



class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies = Movies.query.all()
        result = MoviesSchema(many=True).dump(movies)
        return result, 200
