from flask_restx import Resource, Namespace
from flask import request, jsonify
from app.container import genres_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class Movies(Resource):
    def get(self) -> [dict]:
        return genres_service.get_all(), 200


@genres_ns.route('/<int:gid>/')
class Movies(Resource):
    def get(self, gid: int) -> [dict]:
        return genres_service.get_one(gid), 200
