import streamlit as st


st.title("Welcome to E-Programing")
st.subheader("lets find your ideal language")


program = st.selectbox("Pick you choice: ",["JS","Python","C#","C++","Rust","Golan"])


st.write("This is your favoirte progmranig languge you have choose so far ", program)

