import streamlit as st
import requests

API_KEY = st.secrets["TMDB_API_KEY"]


# Search Movie
def search_movie(movie_name):

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": API_KEY,
        "query": movie_name
    }

    response = requests.get(url, params=params)

    data = response.json()

    if data["results"]:
        return data["results"][0]

    return None


# Fetch Poster
def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    response = requests.get(url)

    data = response.json()

    poster = data.get("poster_path")

    if poster:
        return "https://image.tmdb.org/t/p/w500" + poster

    return None


# Movie Recommendations
def fetch_recommendations(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations"

    params = {
        "api_key": API_KEY
    }

    response = requests.get(url, params=params)

    data = response.json()

    movies = []

    for movie in data["results"][:10]:

        movies.append({

            "title": movie["title"],

            "id": movie["id"],

            "poster": (
                "https://image.tmdb.org/t/p/w500"
                + movie["poster_path"]
                if movie["poster_path"]
                else None
            ),

            "rating": movie["vote_average"],

            "release": movie["release_date"]

        })

    return movies