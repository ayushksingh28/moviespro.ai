import pandas as pd
import streamlit as st
import json
import streamlit.components.v1 as components
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np


st.markdown("<h1 style='text-align: center; color: blue;' >Moviespro.ai</h1>", unsafe_allow_html = True)
st.write("## Organize your movie scripts. Powered by AI.")

movie_plots_path = "American_movie_plots_2005_2021_v1.csv"

@st.cache
def load_data():
    df = pd.read_csv(movie_plots_path)
    df.drop_duplicates(subset = "Wiki link", keep = False, inplace = True)
    return df
    
@st.cache
def get_transformed_output():
    tfidfvectorizer = TfidfVectorizer(analyzer = "word", stop_words = "english")
    tfidfvectorizer.fit(data["Plot"])
    transform_output = tfidfvectorizer.transform(data["Plot"])
    return tfidfvectorizer, transform_output

def get_keywords_tfidf():
    movie_plot = data.iloc[st.session_state.page]["Plot"]
    vectorizer, transf_output = get_transformed_output()
    movie_vector = vectorizer.transform([movie_plot])
    ftr_names = vectorizer.get_feature_names_out()
    feature_array = np.array(ftr_names)
    sorted_indices = np.argsort(movie_vector.toarray()).flatten()[::-1]
    sorted_keywords = feature_array[sorted_indices]
    return sorted_keywords.tolist()

def get_similar_movies(N):
    movie_plot = data.iloc[st.session_state.page]["Plot"]
    vectorizer, transf_output = get_transformed_output()
    index = st.session_state.page
    index = index
    search_vec = transf_output[index]
    cosine_similarities = linear_kernel(search_vec, transf_output).flatten()
    related_docs_indices = cosine_similarities.argsort()[::-1]
    related_docs_indices = list(related_docs_indices)[:N]
    titles = []
    plots = []
    links = []
    for ind in related_docs_indices:
        title = data.iloc[ind]['Movie Name']
        movie_plot = data.iloc[ind]["Plot"]
        link = data.iloc[ind]['Wiki link']
        titles.append(title)
        plots.append(movie_plot)
        links.append(link)
    return titles, plots, links


data = load_data()

st.write("")
if "page" not in st.session_state:
    st.session_state.page = 0


def next_page():
    st.session_state.page += 1

def previous_page():
    st.session_state.page -= 1

page_number = 0
last_page = len(data)

prev, middle, next= st.columns([2, 2 , 2])

if st.session_state.page < last_page:
    next.button(">", on_click = next_page)

else:
    next.write("")

if st.session_state.page > 0:
    prev.button("<", on_click = previous_page)

else:
    prev.write("")

middle.write(f"Page {1+st.session_state.page} of {last_page}")

row = data.iloc[st.session_state.page]
movie_name = row["Movie Name"]
link = row["Wiki link"]
plot = row["Plot"]
st.header(movie_name)
st.write(link)
st.write(plot)

if st.button("Get Keywords"):
    keywords = get_keywords_tfidf()
    keywords = keywords[:10]
    listToStr = " || ".join([str(elem) for elem in keywords])
    st.write(listToStr)

if st.button("Get similar plots"):
    movienames, movieplots, links = get_similar_movies(5)
    for name, plt, li in zip(movienames, movieplots, links):
        st.header(name)
        st.write(li)
        st.write(plt)
        st.makrdown(".....")



