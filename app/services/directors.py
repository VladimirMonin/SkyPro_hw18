from app.dao.directors import DirectorsDAO


class DirectorsService:
    def __init__(self, directors_dao: DirectorsDAO):
        self.directors_dao = directors_dao

    def get_all(self):
        return self.directors_dao.get_all()

    def get_one(self, did):
        return self.directors_dao.get_one(did)

    def get_one_raw(self, did):
        return self.directors_dao.get_one_raw(did)
