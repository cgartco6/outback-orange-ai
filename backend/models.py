from backend.database import db
from datetime import datetime

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    style = db.Column(db.String(50))
    creative_freedom = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Carousel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer)
    content = db.Column(db.Text)
    status = db.Column(db.String(50), default="draft")
    scheduled_time = db.Column(db.DateTime)
