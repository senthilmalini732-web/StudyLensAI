
import streamlit as st

st.set_page_config(page_title="StudyLens AI", page_icon="📚")

st.title("📚 StudyLens AI")
st.subheader("Your Personal AI Study Assistant")

st.write("Welcome! Make your studying easier.")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome to StudyLens AI, {name}!")

st.write("Upload your study notes here.")

notes = st.file_uploader("Choose your notes", type=["txt", "pdf"])

if notes:
    st.success("Your file uploaded successfully!")
