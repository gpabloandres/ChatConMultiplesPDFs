import funciones
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

st.set_page_config("Chat PDF")
st.header("Chat with PDF using Gemini")

user_question = st.text_input("Ask a Question from the PDF Files")
    
if user_question:
    funciones.user_input(user_question)
    
with st.sidebar:
    st.title("Menú: ")
    pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
    if st.button("Submit & Process"):
        with st.spinner("Processing..."):
            raw_text = funciones.get_pdf_text(pdf_docs)
            text_chunks = funciones.get_text_chunks(raw_text)
            funciones.get_vector_store(text_chunks)
            st.success("Done")