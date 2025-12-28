# Movie Recommender System
A content-based Movie Recommendation System built using **FastAPI** for the backend and **Streamlit** for the frontend.
The system recommends similar movies based on content similarity using cosine similarity on TMDB movie data.

## About the Project
This project demonstrates an end-to-end Machine Learning application where a trained recommendation model is served through a REST API and consumed by a web-based interface.
Users can select a movie and receive recommendations for similar movies along with their posters.

## Features
- Content-based movie recommendation
- FastAPI backend for serving recommendations
- Streamlit interactive frontend
- Cosine similarity–based recommendation logic
- TMDB API integration for movie posters
- Clean separation of backend and frontend

## Tech Stack

- **Language:** Python  
- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **Machine Learning:** Scikit-learn  
- **Data Processing:** Pandas, NumPy  
- **API Integration:** TMDB API  

## Project Structure
```
movie-recommender-system/
├── app.py                    # FastAPI backend
├── frontend.py               # Streamlit frontend
├── requirements.txt
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── model/
│   ├── movie_list.pkl
│   └── similarity.pkl
└── README.md
```

## How to Run the Project
### 1. Install dependencies
```
pip install -r requirements.txt
```
### 2. Start the FastAPI backend
```
uvicorn app:app --reload
```
Backend runs at:
```
http://127.0.0.1:8000
```
### 3. Run the Streamlit frontend
```
streamlit run frontend.py
```
## API Endpoints
- `GET /` – API status check  
- `GET /movies` – Get list of all movies  
- `POST /recommend` – Get movie recommendations
  
## Dataset
The project uses TMDB datasets containing movie metadata and credits information.  
Content similarity is calculated using textual features to recommend similar movies.

## Purpose
This project is intended for:
- Learning recommender systems
- Practicing ML model deployment
- Building API-driven ML applications
- Portfolio and GitHub showcase
