import streamlit as st
from ollama_infer import analyze_code_with_ollama
import os



st.set_page_config(page_icon="⚡️",page_title="sana.ai", layout="centered")
st.title("🛠️ sana.ai – Local AI Bug Fix & Code Review Tool")

uploaded_file = st.file_uploader("📁 Upload a Python (.py) file", type=["py"])

if uploaded_file:
    code_content = uploaded_file.read().decode("utf-8")
    st.subheader("📄 Uploaded Code")
    st.code(code_content, language="python")

    if st.button("⚡️ Review Code with AI"):
        with st.spinner("Analyzing code with Mistral via Ollama..."):
            result = analyze_code_with_ollama(code_content)
        st.markdown("---")
        st.subheader("🧾 Review Result")
        st.markdown(result, unsafe_allow_html=True)