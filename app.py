import streamlit as st

from utils.tmdb import search_movie
from utils.tmdb import fetch_recommendations

st.set_page_config(
    page_title="Moviqo AI",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Moviqo AI")
st.subheader("AI Powered Movie Recommendation System")

movie_name = st.text_input(
    "Search Any Movie",
    placeholder="Animal, Leo, Jawan, Interstellar..."
)

if st.button("🔍 Search"):

    movie = search_movie(movie_name)

    if movie is None:

        st.error("Movie not found!")

    else:

        st.success(f'Found: {movie["title"]}')

        st.image(
            "https://image.tmdb.org/t/p/w500" + movie["poster_path"],
            width=250
        )

        st.write("⭐ Rating:", movie["vote_average"])

        st.write("📅 Release:", movie["release_date"])

        st.write(movie["overview"])

        st.divider()

        st.subheader("🎯 Recommended Movies")

        recommendations = fetch_recommendations(movie["id"])

        cols = st.columns(5)

        for index, item in enumerate(recommendations):

            with cols[index % 5]:

                if item["poster"]:

                    st.image(item["poster"])

                st.caption(item["title"])

                st.write("⭐", round(item["rating"], 1))