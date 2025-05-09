import streamlit as st

# Fonction simulée
def ask_gpt(prompt):
    return f"💬 **Réponse simulée :** {prompt}"

# Configuration pro-style
st.set_page_config(page_title="EntreprendIA – Plateforme IA pour Entrepreneurs", layout="wide")

# Bandeau élégant avec effet visuel
top_section = """
<style>
h1, h2, h3, h4 {font-family: 'Helvetica Neue', sans-serif;}
body {background-color: #f4f6f8;}
.main .block-container {padding: 2rem 4rem; background-color: #ffffff; border-radius: 16px; box-shadow: 0 6px 24px rgba(0,0,0,0.12);}
.sidebar .sidebar-content {background-color: #ffffff; border-radius: 16px; padding: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.1);}
.stButton>button {background-color: #0073e6; color: white; border-radius: 8px; font-weight: bold; transition: background-color 0.3s;}
.stButton>button:hover {background-color: #005bb5;}
.stTabs [data-baseweb="tab"] {font-size: 1.1em; font-weight: 600;}
</style>

<div style='text-align: center; padding-bottom: 10px;'>
    <h1 style='font-size:3em;'>🚀 EntreprendIA</h1>
    <h2 style='color: #444;'>Plateforme IA professionnelle pour entrepreneurs ambitieux</h2>
    <p style='font-size:1.1em; max-width: 800px; margin: auto;'>Offrez à vos projets des recommandations stratégiques, financières et marketing basées sur les meilleures données nationales et internationales, avec une interface moderne et fluide.</p>
</div>
<hr>
"""

st.markdown(top_section, unsafe_allow_html=True)

# Sidebar améliorée
st.sidebar.title("🌟 Navigation rapide")
st.sidebar.markdown("""
**Modules inclus :**
- Assistance IA
- Génération d’idées
- Analyse de marché
- Géomarketing
- Simulation financière
- Plan d’affaires

**À venir :**
- Recommandations intelligentes
- Benchmarks sectoriels
- Rapports interactifs téléchargeables
- Tableau de bord avec visualisations dynamiques
""")

# Onglets professionnels
tabs = st.tabs(["🤖 Assistance", "💡 Idées", "📊 Marché", "🗺️ Géomarketing", "📈 Finances", "📝 Plan d'affaires"])

with tabs[0]:
    st.header("🤖 Assistance personnalisée")
    q1 = st.text_input("Votre question :", placeholder="Ex. Comment trouver des financements ?")
    if st.button("Répondre", key="b1") and q1:
        st.success(ask_gpt(q1))

with tabs[1]:
    st.header("💡 Générateur d’idées innovantes")
    secteur = st.text_input("Secteur ciblé :", placeholder="Ex. Tech durable")
    if st.button("Générer", key="b2") and secteur:
        st.success(ask_gpt(f"Idées innovantes dans le secteur : {secteur}"))

with tabs[2]:
    st.header("📊 Analyse de marché avancée")
    secteur_analyse = st.text_input("Secteur à analyser :", placeholder="Ex. Mode éthique")
    if st.button("Analyser", key="b3") and secteur_analyse:
        st.success(ask_gpt(f"Analyse détaillée du marché pour : {secteur_analyse}"))

with tabs[3]:
    st.header("🗺️ Analyse géomarketing détaillée")
    zone = st.text_input("Zone géographique :", placeholder="Ex. Tunis, Sfax")
    if st.button("Analyser zone", key="b4") and zone:
        st.success(ask_gpt(f"Profil géomarketing pour : {zone}"))

with tabs[4]:
    st.header("📈 Simulation financière complète")
    projet = st.text_input("Projet à simuler :", placeholder="Ex. Application mobile santé")
    if st.button("Simuler", key="b5") and projet:
        st.success(ask_gpt(f"Simulation financière complète pour : {projet}"))

with tabs[5]:
    st.header("📝 Génération de plan d’affaires professionnel")
    projet_nom = st.text_input("Nom du projet :", placeholder="Ex. Café bio innovant")
    if st.button("Créer plan d’affaires", key="b6") and projet_nom:
        st.success(ask_gpt(f"Plan d’affaires structuré pour : {projet_nom} (résumé exécutif, marché, stratégie, finances, indicateurs clés, recommandations)"))

st.markdown("""
<hr>
<div style='text-align: center; color: #666;'>
⚠️ **Mode simulateur actif :** Les résultats affichés sont fictifs et illustratifs, à usage de démonstration.
</div>
""", unsafe_allow_html=True)
