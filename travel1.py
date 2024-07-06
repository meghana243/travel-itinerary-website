import streamlit as st

st.set_page_config(page_title="Travel Itinerary", page_icon="🗺️")

st.title("Welcome to the Travel Itinerary Website")

st.sidebar.header("Navigation")
#st.sidebar.page_link("pages/1_home.py", label="Home", icon="🏠")
st.sidebar.page_link("pages/2_travel.py", label="Travel", icon="✈️")
st.sidebar.page_link("pages/3_blogs.py", label="Blogs", icon="📝")
