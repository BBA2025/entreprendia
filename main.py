import streamlit as st

# Fonction simulée au lieu de l'API OpenAI
def ask_gpt(prompt):
    return f"[Réponse simulée] Vous avez demandé : {prompt}"

st.set_page_config(page_title="EntreprendIA (Mode Simulateur)", layout="centered")
st.title("🚀 EntreprendIA – Agent IA pour entrepreneurs (Mode Simulateur)")

tab1, tab2, tab3, tab4 = st.tabs(["Assistance", "Idées", "Analyse Marché", "Géomarketing"])

with tab1:
    st.header("🤖 Assistance entrepreneuriale")
    user_question = st.text_input("Pose ta question entrepreneuriale :")
    if st.button("Obtenir réponse") and user_question:
        answer = ask_gpt(user_question)
        st.write(answer)

with tab2:
    st.header("💡 Génération d'idées")
    secteur = st.text_input("Indique ton secteur d'intérêt :")
    si = st.button("Générer idée")
    if si and secteur:
        ideas = ask_gpt(f"Idées pour le secteur : {secteur}")
        st.write(ideas)

with tab3:
    st.header("📊 Analyse rapide du marché")
    secteur_analyse = st.text_input("Secteur à analyser :")
    if st.button("Analyser le marché") and secteur_analyse:
        analysis = ask_gpt(f"Analyse marché pour : {secteur_analyse}")
        st.write(analysis)

with tab4:
    st.header("🗺️ Géomarketing & zone de chalandise")
    zone = st.text_input("Indique la zone géographique (ville ou région) :")
    if st.button("Analyser la zone") and zone:
        geo_analysis = ask_gpt(f"Analyse géomarketing pour : {zone}")
        st.write(geo_analysis)

st.sidebar.markdown("---")
st.sidebar.write("Prototype initial - Mode Simulateur")
