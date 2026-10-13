
import streamlit as st
from pypdf import PdfReader

st.set_page_config(
    page_title="StudyLens AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 StudyLens AI")
st.subheader("Your Personal AI Study Assistant")
st.write("Learn smarter, not harder! ✨")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome, {name}!")

notes = st.file_uploader(
    "Upload your study notes",
    type=["pdf", "txt"]
)

if notes:
    if notes.name.endswith(".pdf"):
        reader = PdfReader(notes)
        text = "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        )
    else:
        text = notes.getvalue().decode(
            "utf-8", errors="ignore"
        )

    if text.strip():
        st.success("Notes uploaded and read successfully!")

        st.subheader("📖 Your Notes")
        st.text_area("Extracted text", text, height=200)

        if st.button("📝 Generate Short Summary"):
            words = text.split()
            summary = " ".join(words[:100])
            st.subheader("Summary")
            st.write(summary)
            if len(words) > 100:
                st.caption("This is a basic extract, not an AI-generated summary.")

        if st.button("❓ Create Practice Questions"):
            sentences = [
                s.strip() for s in text.replace(
                    "\n", " "
                ).split(".") if len(s.split()) >= 5
            ]

            if sentences:
                for i, sentence in enumerate(sentences[:5], 1):
                    st.write(f"**Question {i}:** Explain this point:")
                    st.info(sentence)
            else:
                st.warning("Not enough text to create questions.")
    else:
        st.warning("No readable text found in this file.")

st.divider()
st.caption("Made with ❤️ | StudyLens AI")
