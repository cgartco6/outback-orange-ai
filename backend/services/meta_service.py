import requests
import os

META_ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")

def post_carousel(page_id, images, captions):
    media_ids = []

    for image in images:
        upload_url = f"https://graph.facebook.com/v18.0/{page_id}/photos"
        response = requests.post(upload_url, data={
            "url": image,
            "published": "false",
            "access_token": META_ACCESS_TOKEN
        })
        media_ids.append(response.json()["id"])

    post_url = f"https://graph.facebook.com/v18.0/{page_id}/feed"
    requests.post(post_url, data={
        "attached_media": [{"media_fbid": mid} for mid in media_ids],
        "message": captions[0],
        "access_token": META_ACCESS_TOKEN
    })
