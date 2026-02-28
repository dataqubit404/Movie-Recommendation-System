import streamlit as st
from tmdb_api import get_trending_movies, get_genres

st.set_page_config(page_title="Movie Recommender", layout="wide")

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


# ------------------ SESSION STATE ------------------
if "selected_movie_id" not in st.session_state:
    st.session_state.selected_movie_id = None

if "search_query" not in st.session_state:
    st.session_state.search_query = ""

if "selected_genre" not in st.session_state:
    st.session_state.selected_genre = None


# ------------------ HEADER ------------------
# -------- HERO SECTION --------

trending_movies = get_trending_movies()

# Floating top 3 posters
st.markdown(f"""
<div class="poster-container">
    <img src="{trending_movies[0]['poster_url']}">
    <img src="{trending_movies[1]['poster_url']}">
    <img src="{trending_movies[2]['poster_url']}">
</div>
""", unsafe_allow_html=True)

# Big Quote
st.markdown("""
<div class="hero-text">
Discover Movies and binge-watch <br>
Without the Hassle
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ------------------ SEARCH SECTION ------------------
col1, col2, col3 = st.columns([3,2,1])

with col1:
    search_query = st.text_input(
    "",
    placeholder="🔍Search through thousands of movies"
)


with col2:
    genres = get_genres()
    genre_dict = {genre["name"]: genre["id"] for genre in genres}
    selected_genre_name = st.selectbox("Select Genre", ["None"] + list(genre_dict.keys()))

with col3:
    if st.button("Search"):
        st.session_state.search_query = search_query
        if selected_genre_name != "None":
            st.session_state.selected_genre = genre_dict[selected_genre_name]
        else:
            st.session_state.selected_genre = None
        st.switch_page("pages/recommendations.py")


st.markdown("---")

# ------------------ TRENDING MOVIES ------------------
st.subheader("Trending Movies")

trending_movies = get_trending_movies()

cols = st.columns(5)

for index, movie in enumerate(trending_movies[:10]):
    with cols[index % 5]:
        st.image(movie["poster_url"], use_container_width=True)
        st.caption(movie["title"])
        if st.button("View", key=f"trending_{movie['id']}"):
            st.session_state.selected_movie_id = movie["id"]
            st.switch_page("pages/movie_detail.py")