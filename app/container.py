from app.dao.movies import MoviesDAO
from app.database import db
from app.services.movies import MoviesService


movies_dao = MoviesDAO(db.session)
movies_service = MoviesService(movies_dao)
