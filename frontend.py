import streamlit as st
import requests

# CONFIG
API_URL = "http://127.0.0.1:8000"
TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

st.set_page_config(
    page_title="Movie Recommender",
    layout="wide"
)

st.title("🎬 Movie Recommender System")

# FETCH MOVIE LIST FROM API
@st.cache_data
def get_movies():
    response = requests.get(f"{API_URL}/movies")
    return response.json()

movie_list = get_movies()

# POSTER FETCH (TMDB)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get("poster_path")

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return None

# CALL RECOMMEND API
def recommend(movie_name):
    response = requests.post(
        f"{API_URL}/recommend",
        json={"movie_name": movie_name}
    )

    if response.status_code != 200:
        return [], []

    data = response.json()["recommendations"]

    names = []
    posters = []

    for item in data:
        names.append(item["title"])
        posters.append(fetch_poster(item["movie_id"]))

    return names, posters

# UI INPUT
selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)

# BUTTON ACTION
if st.button("Show Recommendation"):
    with st.spinner("Finding similar movies..."):
        names, posters = recommend(selected_movie)

    if len(names) == 0:
        st.error("No recommendations found.")
    else:
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(names[i])
                if posters[i]:
                    st.image(posters[i])
                else:
                    st.write("No poster available")