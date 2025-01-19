import requests
import os

from loader import bot
from utils.misc.show_movie import send_info

API_KEY = os.getenv("KINOPOISK_API_KEY")
HEADERS = {
    "accept": "application/json",
    "X-API-KEY": API_KEY
}
KINO_URL = "https://api.kinopoisk.dev/v1.4/"


def get_response(search_type, message=None):
    global KINO_URL
    kino_url = KINO_URL

    if search_type.startswith("movie_"):
        kino_url += "movie/"
        params = {"notNullFields": (
            "id",
            "name",
            "poster.url",
            "description",
            "year",
            "countries.name",
            "genres.name",
            "rating.kp")}

        if "random" in search_type:
            kino_url += "random"
        response = requests.get(kino_url, headers=HEADERS, params=params).json()
        movie_info = {"movie_id": response["id"],
                      "movie_name": response["name"],
                      "movie_poster": response["poster"]["url"],
                      "movie_description": response["description"],
                      "movie_year": response["year"],
                      "movie_country": response["countries"][0]["name"],
                      "movie_genre": response["genres"][0]["name"],
                      "movie_rating": response["rating"]["kp"]}
    send_info(search_type, message.chat.id, movie_info)
