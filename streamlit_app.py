import pandas as pd
import streamlit as st
import json
import streamlit.components.v1 as components


st.markdown("<h1 style='text-align: center; color: blue;' >Moviespro.ai</h1>", unsafe_allow_html = True)
st.write("## Organize your movie scripts. Powered by AI.")

movie_plots_path = "American_movie_plots_2005_2021_v1.csv"

@st.cache
def load_data():
    return pd.read_csv(movie_plots_path)


#Read the data
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

prev, middle, next= st.columns([2, 10, 2])

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