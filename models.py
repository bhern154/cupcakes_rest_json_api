"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """ Cupcake database model as cupcakes_db"""

    # table cupcake inside cupcakes_ub
    __tablename__ = "cupcake"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default='https://tinyurl.com/demo-cupcake')

    def __repr__(self):
        e = self
        return f"<Cupcake {e.id} {e.flavor} {e.size} {e.rating} {e.image}>"