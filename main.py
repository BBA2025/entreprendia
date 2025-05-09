import streamlit as st

# Fonction simulée pour tester sans clé API
def ask_gpt(prompt):
    return f"\n💬 **Réponse simulée :** Vous avez demandé : _{prompt}_\n"

# Configuration de la page
st.set_page_config(page_title="EntreprendIA – Mode Simulateur", layout="wide")

# Bandeau principal
st.markdown("""
<div style='text-align: center;'>
    <h1>🚀 EntreprendIA – Agent IA pour Entrepreneurs</h1>
    <h3 style='color: grey;'>Prototype interactif – Mode Simulateur</h3>
</div>
<hr>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🔧 Navigation")
st.sidebar.info("💡 Passez en mode API pour des réponses réelles.")

# Onglets organisés
tabs = st.tabs(["🤖 Assistance", "💡 Idées", "📊 Analyse Marché", "🗺️ Géomarketing"])

with tabs[0]:
    st.subheader("Assistance entrepreneuriale personnalisée")
    user_question = st.text_input("Posez votre question :", placeholder="Ex. Comment lancer mon activité artisanale ?")
    if st.button("Obtenir une réponse", key="btn1") and user_question:
        answer = ask_gpt(user_question)
        st.success(answer)

with tabs[1]:
    st.subheader("Générateur d'idées innovantes")
    secteur = st.text_input("Secteur d'intérêt :", placeholder="Ex. Économie circulaire")
    if st.button("Générer une idée", key="btn2") and secteur:
        ideas = ask_gpt(f"Idées pour le secteur : {secteur}")
        st.success(ideas)

with tabs[2]:
    st.subheader("Analyse rapide du marché")
    secteur_analyse = st.text_input("Secteur à analyser :", placeholder="Ex. Cosmétique bio")
    if st.button("Lancer l'analyse", key="btn3") and secteur_analyse:
        analysis = ask_gpt(f"Analyse marché pour : {secteur_analyse}")
        st.success(analysis)

with tabs[3]:
    st.subheader("Géomarketing & zone de chalandise")
    zone = st.text_input("Zone géographique (ville ou région) :", placeholder="Ex. Tunis, Sfax")
    if st.button("Analyser la zone", key="btn4") and zone:
        geo_analysis = ask_gpt(f"Analyse géomarketing pour : {zone}")
        st.success(geo_analysis)

st.markdown("""
<hr>
<div style='text-align: center; color: grey;'>
    ⚠️ **Note :** Vous êtes actuellement en mode simulateur. Les réponses affichées sont fictives et destinées à la démonstration.
</div>
""", unsafe_allow_html=True)
