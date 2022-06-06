from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db


def create_app(config: Config) -> Flask:
    application = Flask(__name__)  # Создаем приложение
    application.config.from_object(config)  # Конфигурируем приложение
    print(application.config)
    application.app_context().push()  # Пушим настройки в приложение (у меня работало и так, но лучше не пропускать)
    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    # api.add_namespace(cat_ns) # импорт из from app.views.cats import cat_ns

if __name__ == '__main__':
    app_config = Config()  # Создаем объект кофигурации Фласк from app.config import Config
    app = create_app(app_config)  # Создаем приложение Фласк
    configure_app(app)
    app.run()
