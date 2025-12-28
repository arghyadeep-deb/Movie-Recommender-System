from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle

# Load model files
movies = pickle.load(open("model/movie_list.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))

app = FastAPI(title="Movie Recommender API")

class MovieRequest(BaseModel):
    movie_name: str
    top_n: int = 5

def recommend_movies(movie_name, top_n):
    if movie_name not in movies["title"].values:
        return None

    index = movies[movies["title"] == movie_name].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    result = []
    for i in distances[1:top_n+1]:
        result.append({
            "movie_id": int(movies.iloc[i[0]].movie_id),
            "title": movies.iloc[i[0]].title
        })

    return result

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/movies")
def get_movies():
    return movies["title"].tolist()

@app.post("/recommend")
def recommend(request: MovieRequest):
    result = recommend_movies(request.movie_name, request.top_n)
    if result is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"recommendations": result}