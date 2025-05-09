import streamlit as st

# Fonction simulée pour tester sans clé API
def ask_gpt(prompt):
    return f"\n[Réponse simulée] Vous avez demandé : {prompt}\n"

st.set_page_config(page_title="EntreprendIA (Mode Simulateur)", layout="centered")
st.title("🚀 EntreprendIA – Agent IA pour entrepreneurs (Mode Simulateur)")

# Organisation des onglets
tab1, tab2, tab3, tab4 = st.tabs(["Assistance", "Idées", "Analyse Marché", "Géomarketing"])

with tab1:
    st.header("🤖 Assistance entrepreneuriale")
    user_question = st.text_input("Pose ta question entrepreneuriale :")
    if st.button("Obtenir réponse", key="btn1") and user_question:
        answer = ask_gpt(user_question)
        st.success(answer)

with tab2:
    st.header("💡 Génération d'idées")
    secteur = st.text_input("Indique ton secteur d'intérêt :")
    if st.button("Générer idée", key="btn2") and secteur:
        ideas = ask_gpt(f"Idées pour le secteur : {secteur}")
        st.success(ideas)

with tab3:
    st.header("📊 Analyse rapide du marché")
    secteur_analyse = st.text_input("Secteur à analyser :")
    if st.button("Analyser le marché", key="btn3") and secteur_analyse:
        analysis = ask_gpt(f"Analyse marché pour : {secteur_analyse}")
        st.success(analysis)

with tab4:
    st.header("🗺️ Géomarketing & zone de chalandise")
    zone = st.text_input("Indique la zone géographique (ville ou région) :")
    if st.button("Analyser la zone", key="btn4") and zone:
        geo_analysis = ask_gpt(f"Analyse géomarketing pour : {zone}")
        st.success(geo_analysis)

st.sidebar.markdown("---")
st.sidebar.write("Prototype initial - Mode Simulateur")
st.sidebar.info("💡 Astuce : Passez en mode API pour des réponses réelles.")
