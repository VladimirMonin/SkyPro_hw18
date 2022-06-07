from app.dao.movies import MoviesDAO


class MoviesService:
    def __init__(self, movies_dao: MoviesDAO):
        self.movies_dao = movies_dao

    def get_all(self):
        return self.movies_dao.get_all()

    def get_one(self, mid):
        return self.movies_dao.get_one(mid)

    def create(self, data):
        self.movies_dao.create(data)
        pass

