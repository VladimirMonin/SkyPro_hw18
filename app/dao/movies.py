
from app.dao.models.movies import Movies, MoviesSchema



class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies = Movies.query.all()
        result = MoviesSchema(many=True).dump(movies)
        return result, 200

    def get_one(self, mid):
        movie = Movies.query.one(mid)
        result = MoviesSchema().dump(movie)
        return result, 200

    def create(self, data):
        movie = Movies(**data)
        self.session.add(movie)
        self.session.commit()
        self.session.close()
