from flask_restx import Resource, Namespace
from flask import request, jsonify
from app.container import directors_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class Movies(Resource):
    def get(self) -> [dict]:
        return directors_service.get_all(), 200


@directors_ns.route('/<int:did>/')
class Movies(Resource):
    def get(self, did: int) -> [dict]:
        return directors_service.get_one(did), 200
