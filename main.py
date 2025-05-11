import streamlit as st
from chatbot import generer_reponse

# -- Cette ligne DOIT être en tout premier après les imports --
st.set_page_config(page_title="EntreprendIA – Coach IA Entrepreneurial", layout="wide")

# -- STYLE PERSONNALISÉ --
st.markdown("""
<style>
h1, h2, h3, h4 {font-family: 'Helvetica Neue', sans-serif;}
body {background-color: #f4f6f8;}
.main .block-container {padding: 2rem 4rem; background-color: #ffffff; border-radius: 16px; box-shadow: 0 6px 24px rgba(0,0,0,0.12);}
.sidebar .sidebar-content {background-color: #ffffff; border-radius: 16px; padding: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.1);}
.stButton>button {background-color: #0073e6; color: white; border-radius: 8px; font-weight: bold; transition: background-color 0.3s;}
.stButton>button:hover {background-color: #005bb5;}
</style>
""", unsafe_allow_html=True)

# -- EN-TÊTE PRINCIPALE --
st.markdown("""
<div style='text-align: center;'>
    <h1>🚀 Le coach IA complet pour entrepreneurs ambitieux</h1>
    <p>Avancez étape par étape pour concrétiser votre projet avec l’aide de l’intelligence artificielle.</p>
</div>
<hr>
""", unsafe_allow_html=True)

# -- SIDEBAR INTERACTIVE --
st.sidebar.title("🌟 Tableau de bord")
st.sidebar.markdown("✅ **Étapes complétées :**")
progress = st.sidebar.selectbox("Choose an option", ["", "Chatbot", "Plan", "Analyse", "Simulation"])

st.sidebar.markdown("### Modules disponibles :")
st.sidebar.write("- Chatbot intelligent")
st.sidebar.write("- Générateur de plan d’affaires")
st.sidebar.write("- Analyse de marché")
st.sidebar.write("- Recommandations stratégiques")
st.sidebar.write("- Simulation financière")

# -- ONGLET CENTRAL --
tabs = st.tabs(["💬 Chatbot IA", "📝 Plan d'affaires", "📊 Analyse Marché", "🎯 Recommandations", "📈 Finances"])

with tabs[0]:
    st.header("💬 Chatbot IA")
    question = st.text_input("Posez votre question ici :", placeholder="Ex. Comment lancer mon activité artisanale ?")
    if st.button("Obtenir une réponse IA"):
        if question:
            reponse = generer_reponse(question)
            st.success(reponse)
        else:
            st.warning("Merci d’écrire une question avant d’envoyer.")

with tabs[1]:
    st.header("📝 Générateur de plan d’affaires")
    if st.button("Générer un exemple de plan d’affaires"):
        st.info("Résumé exécutif, marché cible, stratégie, finances, indicateurs clés...")

with tabs[2]:
    st.header("📊 Analyse de marché")
    secteur = st.text_input("Secteur à analyser :", placeholder="Ex. Agroalimentaire")
    if st.button("Lancer l’analyse"):
        st.success(f"Analyse simulée du marché dans le secteur : {secteur}")

with tabs[3]:
    st.header("🎯 Recommandations stratégiques")
    st.write("- Validez vos hypothèses avant investissement")
    st.write("- Analysez la concurrence locale")
    st.write("- Structurez votre plan de financement")

with tabs[4]:
    st.header("📈 Simulation financière")
    chiffre = st.number_input("Chiffre d’affaires prévisionnel (TND)", min_value=0)
    couts = st.number_input("Coûts totaux (TND)", min_value=0)
    if st.button("Calculer marge"):
        if chiffre >= couts:
            marge = chiffre - couts
            st.success(f"Votre marge brute estimée est de {marge} TND")
        else:
            st.error("⚠️ Les coûts dépassent le chiffre d’affaires.")

# -- PIED DE PAGE --
st.markdown("""
<hr>
<div style='text-align: center; color: #666;'>
⚠️ **Mode simulateur actif :** Les résultats affichés sont fictifs. Connectez une clé API valide pour activer l’IA réelle.
</div>
""", unsafe_allow_html=True)
