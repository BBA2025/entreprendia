from chatbot import generer_reponse
import streamlit as st

# --- CONFIGURATION PAGE ---
st.set_page_config(page_title="EntreprendIA – Coach IA Entrepreneurial", layout="wide")

# --- STYLE PERSONNALISÉ ---
st.markdown("""
<style>
h1, h2, h3, h4 {font-family: 'Helvetica Neue', sans-serif;}
body {background-color: #f4f6f8;}
.main .block-container {padding: 2rem 4rem; background-color: #ffffff; border-radius: 16px; box-shadow: 0 6px 24px rgba(0,0,0,0.12);}
.sidebar .sidebar-content {background-color: #ffffff; border-radius: 16px; padding: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.1);}
.stButton>button {background-color: #0073e6; color: white; border-radius: 8px; font-weight: bold; transition: background-color 0.3s;}
.stButton>button:hover {background-color: #005bb5;}
.stProgress > div > div > div {background-color: #0073e6;}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<div style='text-align: center;'>
    <h1>🚀 EntreprendIA</h1>
    <h2 style='color: #444;'>Le coach IA complet pour entrepreneurs ambitieux</h2>
    <p>Avancez étape par étape pour concrétiser votre projet avec l’aide de l’intelligence artificielle.</p>
</div>
<hr>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("🌟 Tableau de bord")
progress = st.sidebar.progress(0)
steps = ["Idée", "Analyse Marché", "Géomarketing", "Finances", "Plan d’Affaires", "Recommandations Finales"]
completed_steps = st.sidebar.multiselect("✅ Étapes complétées :", steps)

# Calculer la progression
progress_value = len(completed_steps) / len(steps)
progress.progress(progress_value)

st.sidebar.markdown("**Modules clés :**")
st.sidebar.write("- Chatbot Assistance")
st.sidebar.write("- Générateur de plan d’affaires")
st.sidebar.write("- Recommandations stratégiques")
st.sidebar.write("- Simulation financière (fictive)")

# --- CHATBOT CENTRALISÉ ---
st.header("🤖 Chatbot Assistance Entrepreneuriale")
user_input = st.text_input("Posez votre question ou décrivez votre projet :", placeholder="Ex. Comment trouver des financements ?")
if st.button("Obtenir une réponse IA"):
    if user_input:
        st.success(f"💬 **Réponse IA simulée :** Voici une réponse simulée à votre demande : _{user_input}_ (dans la vraie version, cette réponse sera enrichie par GPT-4 et des données réelles).")
    else:
        st.warning("Merci de saisir une question pour obtenir une réponse.")

# --- MODULE PLAN D’AFFAIRES ---
st.header("📝 Génération de Plan d’Affaires (simulé)")
if st.button("Générer un exemple de plan d’affaires"):
    st.info("✅ **Résumé Exécutif :** Présentation synthétique du projet, sa mission et ses objectifs.")
    st.info("📊 **Analyse de Marché :** Taille du marché, clients cibles, concurrence identifiée.")
    st.info("📈 **Stratégie :** Proposition de valeur unique, canaux marketing, partenariats.")
    st.info("💰 **Prévisions Financières :** Estimations de revenus, coûts, marge brute, point mort.")
    st.info("🔑 **Indicateurs Clés :** Objectifs chiffrés, jalons et métriques de succès.")
    st.success("Un rapport structuré prêt à être exporté (fonctionnalité future) sera généré ici.")

# --- MODULE RECOMMANDATIONS ---
st.header("🎯 Recommandations Stratégiques Simulées")
if st.button("Obtenir des recommandations clés"):
    st.write("- Consolidez votre proposition de valeur avant de lancer des investissements majeurs.")
    st.write("- Priorisez une analyse de la zone de chalandise pour vérifier la demande locale.")
    st.write("- Formalisez vos hypothèses financières pour identifier vos besoins de financement.")
    st.write("- Préparez un pitch deck synthétique pour présenter aux partenaires ou investisseurs.")

# --- MESSAGE EN BAS DE PAGE ---
st.markdown("""
<hr>
<div style='text-align: center; color: #666;'>
⚠️ **Mode simulateur :** Les résultats affichés sont fictifs, à usage démonstratif uniquement.
</div>
""", unsafe_allow_html=True)
