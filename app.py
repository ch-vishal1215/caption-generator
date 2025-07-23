# app.py

import streamlit as st

st.title("Instagram Caption Generator")

category = st.selectbox("Choose a category", ["Travel", "Food", "Fitness", "Dogs", "Love", "Funny"])

if st.button("Generate Caption"):
    if category == "Travel":
        st.write("Wander often, wonder always ✈️🌍")
    elif category == "Food":
        st.write("Good food = good mood 🍕🍣")
    elif category == "Fitness":
        st.write("No pain, no pizza. Or wait... both? 🏋️‍♂️🍕")
    elif category == "Dogs":
        st.write("Life’s better with a wagging tail 🐶❤️")
    elif category == "Love":
        st.write("Falling for you more every day 💘")
    elif category == "Funny":
        st.write("I put the ‘pro’ in procrastinate 😎")
