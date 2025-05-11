import openai
import streamlit as st

# Utilisation de la clé OpenRouter depuis secrets.toml
openai.api_key = st.secrets["OPENROUTER_API_KEY"]
openai.api_base = "https://openrouter.ai/api/v1"

def generer_reponse(message):
    try:
        completion = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",  # ou un autre modèle supporté
            messages=[
                {"role": "system", "content": "Tu es un coach IA pour entrepreneurs."},
                {"role": "user", "content": message}
            ]
        )
        return completion.choices[0].message["content"]
    except Exception as e:
        return f"❌ Erreur IA : {e}"
