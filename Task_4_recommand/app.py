import pickle
import streamlit as st
import requests
from dotenv import load_dotenv
import os
import gzip

load_dotenv()
API_MOVIE = os.environ.get("API_MOVIE")
URL=os.environ.get("URL")

def fetch_movie_details(movie_id):
    url = URL.format(movie_id,API_MOVIE)
    data = requests.get(url)
    data = data.json()
    return data['title'], data['overview'], "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        title, overview, poster_url = fetch_movie_details(movie_id)
        recommended_movies.append({'title': title, 'overview': overview, 'poster_url': poster_url})

    return recommended_movies

st.header('Discover Your Next Movie with our Recommender System')

movies = pickle.load(open('D:\mine\Codsoft\CODSOFT\Task_4\pickled\movie_list.pkl', 'rb'))
gzip_pkl_file_path = 'D:\mine\Codsoft\CODSOFT\Task_4\pickled\similarity.pkl.gz'
with gzip.open(gzip_pkl_file_path, 'rb') as gzip_file:
    similarity = pickle.load(gzip_file)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Choose or type the name of a movie",
    movie_list
)

if st.button('Get Recommendations'):
    recommended_movies = recommend(selected_movie)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(recommended_movies[i]['title'])
            st.image(recommended_movies[i]['poster_url'], use_column_width=True, caption=recommended_movies[i]['overview'][:100] + '...' if len(recommended_movies[i]['overview']) > 100 else recommended_movies[i]['overview'], clamp=True)
