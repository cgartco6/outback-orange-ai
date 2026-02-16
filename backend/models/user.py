from backend.extensions import db
import uuid

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = db.Column(db.String, db.ForeignKey("tenants.id"))
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(255))
    role = db.Column(db.String(50), default="owner")
