from flask_restx import Resource, Namespace
from flask import request
from app.container import movies_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class Movies(Resource):
    def get(self) -> [dict]:
        return movies_service.get_all(), 200

    def post(self):
        data = request.get_json()
        movies_service.create(data)
        return '', 201

@movies_ns.route('<int:mid>')
class Movies(Resource):
    def get(self, mid) -> [dict]:
        return movies_service.get_one(mid), 200
