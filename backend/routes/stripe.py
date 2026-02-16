from flask import Blueprint, request
import stripe
import os
from backend.extensions import db
from backend.models.subscription import Subscription

stripe_bp = Blueprint("stripe", __name__)

endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

@stripe_bp.route("/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")

    event = stripe.Webhook.construct_event(
        payload, sig_header, endpoint_secret
    )

    if event["type"] == "invoice.paid":
        subscription_id = event["data"]["object"]["subscription"]
        # activate subscription

    return {"status": "success"}
