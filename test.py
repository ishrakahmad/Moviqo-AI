from utils.tmdb import search_movie
from utils.tmdb import fetch_recommendations

movie = search_movie("Animal")

print(movie)

print()

recommendations = fetch_recommendations(movie["id"])

for item in recommendations:

    print(item)