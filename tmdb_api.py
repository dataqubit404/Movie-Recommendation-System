import requests
import streamlit as st
from config import TMDB_API_KEY

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"


# ---------------------- FETCH DATA ----------------------

import time

def fetch_data(endpoint, params=None):
    if params is None:
        params = {}

    params["api_key"] = TMDB_API_KEY
    url = f"{BASE_URL}{endpoint}"

    retries = 3

    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.ConnectionError:
            if attempt < retries - 1:
                time.sleep(1)
                continue
            st.error("Network connection error. Please check your internet.")
            return {}

        except requests.exceptions.Timeout:
            if attempt < retries - 1:
                time.sleep(1)
                continue
            st.error("Request timed out. Try again.")
            return {}

        except requests.exceptions.RequestException as e:
            st.error(f"API Error: {e}")
            return {}



# ---------------------- FORMAT MOVIE ----------------------

def format_movie_data(movie):
    return {
        "id": movie.get("id"),
        "title": movie.get("title"),
        "poster_url": IMAGE_BASE_URL + movie["poster_path"]
        if movie.get("poster_path")
        else None,
        "release_date": movie.get("release_date"),
        "rating": movie.get("vote_average"),
        "overview": movie.get("overview")
    }


# ---------------------- TRENDING ----------------------

@st.cache_data(ttl=600)
def get_trending_movies():
    data = fetch_data("/trending/movie/week")
    return [format_movie_data(m) for m in data.get("results", [])]


# ---------------------- SEARCH ----------------------

@st.cache_data(ttl=600)
def search_movie(query):
    data = fetch_data("/search/movie", {"query": query})
    return [format_movie_data(m) for m in data.get("results", [])]


# ---------------------- SIMILAR ----------------------

@st.cache_data(ttl=600)
def get_similar_movies(movie_id):
    data = fetch_data(f"/movie/{movie_id}/similar")
    return [format_movie_data(m) for m in data.get("results", [])]


# ---------------------- DETAILS ----------------------

@st.cache_data(ttl=600)
def get_movie_details(movie_id):
    data = fetch_data(f"/movie/{movie_id}")
    return format_movie_data(data)


# ---------------------- CAST ----------------------

@st.cache_data(ttl=600)
def get_movie_cast(movie_id):
    data = fetch_data(f"/movie/{movie_id}/credits")
    cast = data.get("cast", [])

    formatted_cast = []
    for actor in cast[:12]:
        formatted_cast.append({
            "name": actor.get("name"),
            "profile_url": IMAGE_BASE_URL + actor["profile_path"]
            if actor.get("profile_path")
            else None
        })

    return formatted_cast


# ---------------------- TRAILER ----------------------

@st.cache_data(ttl=600)
def get_movie_trailer(movie_id):
    data = fetch_data(f"/movie/{movie_id}/videos")
    results = data.get("results", [])

    for video in results:
        if video["type"] == "Trailer" and video["site"] == "YouTube":
            return f"https://www.youtube.com/watch?v={video['key']}"

    return None


# ---------------------- GENRES ----------------------

@st.cache_data(ttl=600)
def get_genres():
    data = fetch_data("/genre/movie/list")
    return data.get("genres", [])


# ---------------------- GENRE MOVIES ----------------------

@st.cache_data(ttl=600)
def get_movies_by_genre(genre_id):
    data = fetch_data("/discover/movie", {"with_genres": genre_id})
    return [format_movie_data(m) for m in data.get("results", [])]
