import streamlit as st
import requests

# Clé API sécurisée via secrets.toml
api_key = st.secrets["OPENROUTER_API_KEY"]

def generer_reponse(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct",  # Tu peux changer le modèle ici si tu veux
        "messages": [
            {"role": "system", "content": "Tu es un assistant IA pour entrepreneurs."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"❌ Erreur API {response.status_code} : {response.text}"
    except Exception as e:
        return f"❌ Erreur de connexion : {str(e)}"
