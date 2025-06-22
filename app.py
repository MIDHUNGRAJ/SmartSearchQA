import streamlit as st
from agent import run_query

st.set_page_config(page_title="SmartSearchQA", layout="centered")
st.title("🔎 SmartSearchQA")

query = st.text_input("Enter your question:", "")

if st.button("Search") and query.strip():
    with st.spinner("Searching and thinking..."):
        try:
            result = run_query(query)
            st.success("Answer:")
            st.write(result)
        except Exception as e:
            st.error(f"Error: {e}")
