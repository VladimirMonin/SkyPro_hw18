from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db
from app.views.directors import directors_ns
from app.views.genres import genres_ns
from app.views.movies import movies_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)  # Создаем приложение
    application.config.from_object(config)  # Конфигурируем приложение
    print(application.config)  # Выводим параметры из конфига в консоль
    application.app_context().push()  # Пушим настройки в приложение (у меня работало и так, но лучше не пропускать)
    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(movies_ns)  # импорт _ns
    api.add_namespace(genres_ns)  # импорт _ns
    api.add_namespace(directors_ns)  # импорт _ns


if __name__ == '__main__':
    app_config = Config()  # Создаем объект кофигурации Фласк from app.config import Config
    app = create_app(app_config)  # Создаем приложение Фласк
    configure_app(app)
    app.run()