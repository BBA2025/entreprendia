import openai
import streamlit as st

# 🔐 Récupère la clé OpenRouter depuis secrets.toml
openai.api_key = st.secrets["OPENROUTER_API_KEY"]
openai.api_base = "https://openrouter.ai/api/v1"

def generer_reponse(message_utilisateur):
    try:
        reponse = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",  # Tu peux tester aussi "openchat/openchat-3.5-1210"
            messages=[
                {"role": "system", "content": "Tu es un assistant IA pour entrepreneurs, clair, pratique et motivant."},
                {"role": "user", "content": message_utilisateur}
            ]
        )
        return reponse["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Erreur IA : {e}"
