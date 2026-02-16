from backend.extensions import db
import uuid

class Tenant(db.Model):
    __tablename__ = "tenants"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(120), nullable=False)
    plan = db.Column(db.String(50), default="free")
    stripe_customer_id = db.Column(db.String(120))
