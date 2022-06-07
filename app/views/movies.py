from flask_restx import Resource, Namespace

from app.container import movies_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class Movies(Resource):
    def get(self):
        movies = movies_service.get_all()
        return movies, 200

    def post(self):
        pass
        # return '', 201

