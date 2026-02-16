from flask import Flask, request, jsonify
from backend.config import Config
from backend.database import db
from backend.models import Client, Carousel
from backend.ai_engine import generate_carousel
from backend.social_poster import sandbox_post_carousel
from backend.scheduler import scheduler
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/intake", methods=["POST"])
def intake():
    data = request.json

    client = Client(
        name=data["name"],
        email=data["email"],
        style=data.get("style", "Modern"),
        creative_freedom=data.get("creative_freedom", False)
    )
    db.session.add(client)
    db.session.commit()

    carousel = generate_carousel(
        client.id,
        theme="Marketing Campaign",
        style=client.style,
        creative_freedom=client.creative_freedom
    )

    sandbox_post_carousel(carousel)

    return jsonify({"message": "Draft created", "carousel": carousel})

@app.route("/approve/<int:carousel_id>", methods=["POST"])
def approve(carousel_id):
    carousel = Carousel.query.get(carousel_id)
    carousel.status = "approved"
    db.session.commit()
    return jsonify({"message": "Approved"})

@app.route("/schedule/<int:carousel_id>", methods=["POST"])
def schedule(carousel_id):
    carousel = Carousel.query.get(carousel_id)
    time = request.json["scheduled_time"]
    scheduled_time = datetime.fromisoformat(time)
    carousel.scheduled_time = scheduled_time
    db.session.commit()
    return jsonify({"message": "Scheduled"})
