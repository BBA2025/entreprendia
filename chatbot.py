import openai
import streamlit as st

# Récupère la clé depuis secrets.toml
openai.api_key = st.secrets["OPENROUTER_API_KEY"]
openai.api_base = "https://openrouter.ai/api/v1"

def generer_reponse(prompt):
    try:
        reponse = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",
            messages=[
                {"role": "system", "content": "Tu es un assistant IA pour entrepreneurs."},
                {"role": "user", "content": prompt}
            ]
        )
        return reponse.choices[0].message["content"]
    except Exception as e:
        return f"⚠️ Erreur IA : {e}"
