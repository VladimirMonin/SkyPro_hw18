from app.database import db
from marshmallow import Schema, fields


class Genres(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class GenresSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
