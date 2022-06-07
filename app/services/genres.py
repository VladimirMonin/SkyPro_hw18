from app.dao.genres import GenresDAO


class GenresService:
    def __init__(self, genres_dao: GenresDAO):
        self.genres_dao = genres_dao

    def get_all(self):
        return self.genres_dao.get_all()

    def get_one(self, gid):
        return self.genres_dao.get_one(gid)

    def get_one_raw(self, gid):
        return self.genres_dao.get_one_raw(gid)
