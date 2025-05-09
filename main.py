import streamlit as st

# Fonction simulée pour tester sans clé API (aucune clé nécessaire)
def ask_gpt(prompt):
    return f"\n[Réponse simulée] Vous avez demandé : {prompt}\n"

st.set_page_config(page_title="EntreprendIA (Mode Simulateur)", layout="centered")
st.title("🚀 EntreprendIA – Agent IA pour entrepreneurs (Mode Simulateur)")

# Message d’accueil
st.write("Bienvenue sur le simulateur d’agent IA pour entrepreneurs. Posez vos questions ou explorez les onglets pour tester !")

# Organisation des onglets
tab1, tab2, tab3, tab4 = st.tabs(["Assistance", "Idées", "Analyse Marché", "Géomarketing"])

with tab1:
    st.header("🤖 Assistance entrepreneuriale")
    user_question = st.text_input("Pose ta question entrepreneuriale :", key="input1")
    if st.button("Obtenir réponse", key="btn1") and user_question:
        answer = ask_gpt(user_question)
        st.success(answer)

with tab2:
    st.header("💡 Génération d'idées")
    secteur = st.text_input("Indique ton secteur d'intérêt :", key="input2")
    if st.button("Générer idée", key="btn2") and secteur:
        ideas = ask_gpt(f"Idées pour le secteur : {secteur}")
        st.success(ideas)

with tab3:
    st.header("📊 Analyse rapide du marché")
    secteur_analyse = st.text_input("Secteur à analyser :", key="input3")
    if st.button("Analyser le marché", key="btn3") and secteur_analyse:
        analysis = ask_gpt(f"Analyse marché pour : {secteur_analyse}")
        st.success(analysis)

with tab4:
    st.header("🗺️ Géomarketing & zone de chalandise")
    zone = st.text_input("Indique la zone géographique (ville ou région) :", key="input4")
    if st.button("Analyser la zone", key="btn4") and zone:
        geo_analysis = ask_gpt(f"Analyse géomarketing pour : {zone}")
        st.success(geo_analysis)

st.sidebar.markdown("---")
st.sidebar.write("Prototype initial - Mode Simulateur")
st.sidebar.info("💡 Astuce : Ce mode n'a pas besoin de clé API. Vous pouvez passer en mode réel plus tard.")

st.write("⚠️ **Note** : Vous êtes actuellement en mode simulateur. Les réponses affichées sont fictives.")
