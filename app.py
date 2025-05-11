import streamlit as st
from summarizer import summarize_text

# Streamlit Interface
st.title("AI Meeting Summarizer")

uploaded_file = st.file_uploader("Please upload the meeting transcript.", type="txt")

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.subheader("Uploaded Text:")
    st.write(text)
    
    # summary
    summary = summarize_text(text)
    st.subheader("Summary:")
    st.write(summary)
