import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_customer(email, tenant_id):
    customer = stripe.Customer.create(
        email=email,
        metadata={"tenant_id": tenant_id}
    )
    return customer

def create_subscription(customer_id, price_id):
    subscription = stripe.Subscription.create(
        customer=customer_id,
        items=[{"price": price_id}]
    )
    return subscription
