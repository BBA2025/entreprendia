import streamlit as st
from chatbot import generer_reponse

# Configuration de la page
st.set_page_config(page_title="EntreprendIA – Coach IA", layout="wide")

# Style personnalisé
st.markdown("""
<style>
h1, h2, h3, h4 {font-family: 'Helvetica Neue', sans-serif;}
body {background-color: #f4f6f8;}
.main .block-container {
    padding: 2rem 4rem;
    background-color: #ffffff;
    border-radius: 16px;
    box-shadow: 0 6px 24px rgba(0,0,0,0.12);
}
.sidebar .sidebar-content {
    background-color: #ffffff;
    border-radius: 16px;
    padding: 1rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.stButton>button {
    background-color: #0073e6;
    color: white;
    border-radius: 8px;
    font-weight: bold;
    transition: background-color 0.3s;
}
.stButton>button:hover {
    background-color: #005bb5;
}
</style>
""", unsafe_allow_html=True)

# En-tête
st.markdown("""
<div style='text-align: center;'>
    <h1>🚀 EntreprendIA</h1>
    <h2 style='color: #444;'>Le coach IA complet pour entrepreneurs</h2>
</div>
<hr>
""", unsafe_allow_html=True)

# Onglets
onglets = st.tabs(["💬 Chatbot IA", "📊 Analyse de Marché", "📈 Simulation financière"])

# --- Onglet 1 : Chatbot IA ---
with onglets[0]:
    st.header("💬 Chatbot IA")
    question = st.text_input("Posez votre question ici :", placeholder="Ex. Comment obtenir un financement ?")

    if st.button("Envoyer", key="send_chatbot"):
        if question:
            reponse = generer_reponse(question)
            st.success(reponse)
        else:
            st.warning("Merci de poser une question pour démarrer.")

# --- Onglet 2 : Analyse marché ---
with onglets[1]:
    st.header("📊 Analyse de marché")
    st.write("📌 Ce module affichera prochainement des données sectorielles enrichies.")

# --- Onglet 3 : Simulation financière ---
with onglets[2]:
    st.header("📈 Simulation financière simplifiée")
    revenu = st.number_input("Revenus mensuels estimés (en TND)", min_value=0)
    couts = st.number_input("Coûts mensuels estimés (en TND)", min_value=0)

    if st.button("Simuler", key="simu"):
        benefice = revenu - couts
        st.metric("Résultat mensuel prévisionnel", f"{benefice} TND")
        if benefice >= 0:
            st.success("Bonne nouvelle ! Vous êtes rentable.")
        else:
            st.error("Attention, vos charges dépassent vos revenus.")

# Bas de page
st.markdown("<hr><center>⚠️ Mode démonstration – API OpenRouter requise pour réponses réelles.</center>", unsafe_allow_html=True)
