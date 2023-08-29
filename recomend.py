import streamlit as st 
import pickle
import pandas as pd

movie_dist =pickle.load(open("df.pkl","rb"))
movie_df = pd.DataFrame(movie_dist)

similarity =pickle.load(open("similarity.pkl","rb"))



def feacth_poster(id):
    import requests

    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMGJiNmUxMmVkODdkOTE1M2Q3YzExYWQzYzAyMjI3OCIsInN1YiI6IjY0ZWNkNDU5NTk0Yzk0MDBhY2IxNmQ4NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.qJxYmQ4oAlmt6DcAWNxux74KuHgZMHD2tr6L_ONSwwY"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    return "https://image.tmdb.org/t/p/w500"+data["poster_path"]


def recomend(movie):
    movie_index = movie_df[movie_df["title"] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True, key= lambda x:x[1])[1:6] 

    recommend_movies = []
    recomended_movies_poster =[]
    for i in movie_list:
        recomended_movies_poster.append(feacth_poster(movie_df.iloc[i[0]].movie_id))
        recommend_movies.append(movie_df.iloc[i[0]].title)
    return recommend_movies ,recomended_movies_poster


st.title("Movie Recomender system")

option = st.selectbox(
    'Emter the movie you like?',
    movie_df["title"])


if st.button("recomend"):
    recomended_movies,recomended_movies_poster = recomend(option)
    col1 , col2 = st.columns(2,gap ="medium")

    for i in range(len(recomended_movies)):
        if i%2==0:
            with col1:
                st.header(recomended_movies[i])
                st.image(recomended_movies_poster[i])
        else:
            with col2:
                st.header(recomended_movies[i])
                st.image(recomended_movies_poster[i])
        




