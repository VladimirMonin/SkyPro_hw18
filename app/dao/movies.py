from app.dao.models.movies import Movies, MoviesSchema


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies = Movies.query.all()
        result = MoviesSchema(many=True).dump(movies)
        return result, 200

    def get_one(self, mid):
        movie = Movies.query.get(mid)
        result = MoviesSchema().dump(movie)
        return result, 200

    def get_one_raw(self, mid):
        movie = Movies.query.get(mid)
        return movie

    def create(self, data):
        movie = Movies(**data)
        self.session.add(movie)
        self.session.commit()
        self.session.close()

    def update(self, data):
        self.session.add(data)
        self.session.commit()

    def delete(self, mid):
        data = self.get_one(mid)
        self.session.delete(data)
        self.session.commit()
