from app.dao.models.genres import Genres, GenresSchema


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genres = Genres.query.all()
        result = GenresSchema(many=True).dump(genres)
        return result, 200

    def get_one(self, gid):
        genre = Genres.query.get(gid)
        result = GenresSchema().dump(genre)
        return result, 200

    def get_one_raw(self, gid):
        genre = Genres.query.get(gid)
        return genre
