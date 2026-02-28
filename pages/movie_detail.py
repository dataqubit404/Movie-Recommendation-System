import streamlit as st
from tmdb_api import (
    get_movie_details,
    get_movie_cast,
    get_movie_trailer
)

st.set_page_config(page_title="Movie Detail", layout="wide")

# ------------------ BACK BUTTON ------------------
if st.button("← Back to Recommendations"):
    st.switch_page("pages/recommendations.py")

movie_id = st.session_state.selected_movie_id

if not movie_id:
    st.warning("No movie selected.")
    st.stop()

# ------------------ FETCH DATA ------------------
movie = get_movie_details(movie_id)
cast = get_movie_cast(movie_id)
trailer_url = get_movie_trailer(movie_id)

# ------------------ MAIN LAYOUT ------------------
col1, col2 = st.columns([1,2])

with col1:
    st.image(movie["poster_url"], use_container_width=True)

with col2:
    st.title(movie["title"])
    st.write("Release Date:", movie["release_date"])
    st.write("Rating:", movie["rating"])
    st.write(movie["overview"])

# ------------------ TRAILER ------------------
if trailer_url:
    st.subheader("Trailer")
    st.video(trailer_url)

# ------------------ CAST ------------------
st.markdown("<h2 style='color:white;'>Top Cast</h2>", unsafe_allow_html=True)
st.markdown("<div class='cast-section'>", unsafe_allow_html=True)


cast_cols = st.columns(6)

for index, actor in enumerate(cast[:12]):
    with cast_cols[index % 6]:
        st.image(actor["profile_url"], use_container_width=True)
        st.caption(actor["name"])
        st.markdown("</div>", unsafe_allow_html=True)

