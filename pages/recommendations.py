import streamlit as st
from tmdb_api import (
    search_movie,
    get_similar_movies,
    get_movies_by_genre
)

st.set_page_config(page_title="Recommendations", layout="wide")

# ------------------ BACK BUTTON ------------------
if st.button("← Back to Home"):
    st.switch_page("app.py")

st.markdown("<h1 style='text-align:center;color:white;'>Recommended Movies</h1>", unsafe_allow_html=True)
st.markdown("---")

movies_to_display = []

# ------------------ SEARCH BY NAME ------------------
if st.session_state.search_query:

    search_results = search_movie(st.session_state.search_query)

    # Take top 3 search results
    for movie in search_results[:3]:
        similar_movies = get_similar_movies(movie["id"])
        movies_to_display.extend(similar_movies)

# ------------------ SEARCH BY GENRE ------------------
elif st.session_state.selected_genre:

    movies_to_display = get_movies_by_genre(st.session_state.selected_genre)

# ------------------ REMOVE DUPLICATES ------------------
unique_movies = {movie["id"]: movie for movie in movies_to_display}
movies_to_display = list(unique_movies.values())

# ------------------ DISPLAY GRID ------------------
cols = st.columns(5)

for index, movie in enumerate(movies_to_display):
    with cols[index % 5]:
        st.image(movie["poster_url"], use_container_width=True)
        st.caption(movie["title"])
        if st.button("View", key=f"rec_{movie['id']}"):
            st.session_state.selected_movie_id = movie["id"]
            st.switch_page("pages/movie_detail.py")
