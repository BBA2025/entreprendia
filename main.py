import streamlit as st
import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

st.set_page_config(page_title="EntreprendIA", layout="centered")
st.title("🚀 EntreprendIA – Agent IA pour entrepreneurs")

tab1, tab2, tab3, tab4 = st.tabs(["Assistance", "Idées", "Analyse Marché", "Géomarketing"])

with tab1:
    st.header("🤖 Assistance entrepreneuriale")
    user_question = st.text_input("Pose ta question entrepreneuriale :")
    if st.button("Obtenir réponse") and user_question:
        prompt = f"Agis comme un expert en création d'entreprise en Tunisie. Réponds clairement à : {user_question}"
        answer = ask_gpt(prompt)
        st.write(answer)

with tab2:
    st.header("💡 Génération d'idées")
    secteur = st.text_input("Indique ton secteur d'intérêt :")
    si = st.button("Générer idée")
    if si and secteur:
        prompt = f"Propose-moi trois idées d'entreprise innovantes en Tunisie dans le secteur suivant : {secteur}."
        ideas = ask_gpt(prompt)
        st.write(ideas)

with tab3:
    st.header("📊 Analyse rapide du marché")
    secteur_analyse = st.text_input("Secteur à analyser :")
    if st.button("Analyser le marché") and secteur_analyse:
        prompt = f"Fournis-moi une analyse rapide des tendances, opportunités et risques actuels dans le secteur {secteur_analyse} en Tunisie."
        analysis = ask_gpt(prompt)
        st.write(analysis)

with tab4:
    st.header("🗺️ Géomarketing & zone de chalandise")
    zone = st.text_input("Indique la zone géographique (ville ou région) :")
    if st.button("Analyser la zone") and zone:
        prompt = f"Donne-moi une analyse simplifiée des opportunités commerciales et du profil de clientèle pour la zone suivante en Tunisie : {zone}."
        geo_analysis = ask_gpt(prompt)
        st.write(geo_analysis)

st.sidebar.markdown("---")
st.sidebar.write("Prototype initial - Sprint 1")
