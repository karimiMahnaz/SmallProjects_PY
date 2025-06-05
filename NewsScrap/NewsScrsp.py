import requests
import streamlit as st


st.title("News Scraper")
tt = st.text_input("which news you want to search")

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-01&sortBy=publishedAt&apiKey=API_KEY"