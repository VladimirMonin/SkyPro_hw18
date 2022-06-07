from app.dao.models.directors import Directors, DirectorsSchema


class DirectorsDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        directors = Directors.query.all()
        result = DirectorsSchema(many=True).dump(directors)
        return result, 200

    def get_one(self, did):
        director = Directors.query.get(did)
        result = DirectorsSchema().dump(director)
        return result, 200

    def get_one_raw(self, did):
        director = Directors.query.get(did)
        return director