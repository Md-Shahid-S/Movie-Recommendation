import pandas as pd
import streamlit as st
import pickle 
import requests

movies = pickle.load(open(r"C:\Md Shahid\Liabilities\Machine Learning Projects\Movie Recommendation System\src\movies.pkl", "rb"))
similarity = pickle.load(open(r"C:\Md Shahid\Liabilities\Machine Learning Projects\Movie Recommendation System\src\similarity.pkl", "rb"))

# convert to DataFrame
movies = pd.DataFrame(movies)

def clean_title(raw_title):
    return raw_title.replace("_", " ").strip()

# OMDb API function
def fetch_poster(movie_title):
    api_key =  " your OMDb key "
    movie_title = clean_title(movie_title)
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data.get("Poster") and data["Poster"] != "N/A":
        return data["Poster"]
    else:
        return "https://via.placeholder.com/300x450.png?text=No+Poster+Found"
# now get titles directly
movies_lst = movies['title'].values
def recommend(movie):
    movie_i = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_i]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    recommended_posters = []
    for i in movies_list:
        raw_title = movies.iloc[i[0]]['title']
        recommend_movies.append(clean_title(raw_title))
        recommended_posters.append(fetch_poster(raw_title))

    return recommend_movies, recommended_posters


# Streamlit App
st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a Movie to Get Recommendations:",
    movies['title'].values,
    format_func=clean_title 
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])

            st.image(posters[idx])
