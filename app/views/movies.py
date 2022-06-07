from flask_restx import Resource, Namespace
from flask import request, jsonify
from app.container import movies_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class Movies(Resource):
    def get(self) -> [dict]:
        return movies_service.get_all(), 200

    def post(self):
        data = request.get_json()
        movies_id = data['id']  # Получаем ID из запроса (которого там может и не быть, т.к. автоинкремент работает!)
        movies_service.create(data)   # Создаем новую запись в БД
        #TODO Сделать по красоте - чтобы POST Работал без передачи IP с запросом
        response = jsonify()  # Делаем пункт из ДЗ \\ Заголовок Location есть в POST на создание сущности.
        response.status_code = 201  # Код ответа
        response.headers['location'] = f'movies/{movies_id}'  # Адрес для "перехода" после добавления
        return response

@movies_ns.route('/<int:mid>/')
class Movies(Resource):
    def get(self, mid: int) -> [dict]:
        return movies_service.get_one(mid), 200

    def put(self, mid: int):
        data = request.json
        data['id'] = mid
        movies_service.update(data)
        return '', 204

    def patch(self, mid: int):
        data = request.json
        data['id'] = mid
        movies_service.update_partial(data)
        return '', 204

    def delete(self, mid: int):
        movies_service.delete(mid)
        return '', 204



