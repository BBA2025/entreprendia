from chatbot import generer_reponse
from fpdf import FPDF
import streamlit as st
import tempfile
import os

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
steps = ["Idée", "Analyse Marché", "Géomarketing", "Finances", "Plan d’Affaires", "Recommandations Finales"]
completed_steps = st.sidebar.multiselect("✅ Étapes complétées :", steps)
progress_value = len(completed_steps) / len(steps) if steps else 0
st.sidebar.progress(progress_value)

st.sidebar.markdown("**Modules disponibles :**")
st.sidebar.write("- Chatbot intelligent")
st.sidebar.write("- Générateur de plan d’affaires")
st.sidebar.write("- Analyse de marché")
st.sidebar.write("- Recommandations stratégiques")
st.sidebar.write("- Simulation financière")

# --- ONGLET PRINCIPAUX ---
tabs = st.tabs([
    "💬 Chatbot IA",
    "📝 Plan d'affaires",
    "📊 Analyse Marché",
    "🎯 Recommandations",
    "📈 Finances"
])

# --- CHATBOT ---
with tabs[0]:from chatbot import generer_reponse

    st.header("💬 Chatbot IA")
    question = st.text_input("Votre question :", key="chatbot_input")
    if st.button("Envoyer", key="send_chatbot"):
        if question:
            reponse = generer_reponse(question)
            st.success(f"💬 {reponse}")
        else:
            st.warning("Merci de saisir une question.")
st.header("💬 Chatbot IA connecté à OpenRouter")

question = st.text_input("Pose ta question ici :", placeholder="Ex. Comment lancer un commerce à Sfax ?")

if st.button("Envoyer la question"):
    if question:
        reponse = generer_reponse(question)
        st.success(reponse)
    else:
        st.warning("Merci d’écrire une question avant de cliquer.")

# --- PLAN D’AFFAIRES ---
with tabs[1]:
    st.header("📝 Plan d’affaires simulé")
    if st.button("Générer un exemple"):
        st.info("✅ **Résumé Exécutif** : Mission et objectifs.")
        st.info("📊 **Analyse de Marché** : Taille, clientèle, concurrence.")
        st.info("📈 **Stratégie** : Positionnement, canaux, modèle économique.")
        st.info("💰 **Prévisions Financières** : Revenus, coûts, marge, rentabilité.")
        st.info("🔑 **Indicateurs Clés** : Objectifs chiffrés, jalons.")
        st.success("📄 Rapport généré avec succès ! (version simulée)")

# --- ANALYSE DE MARCHÉ ---
with tabs[2]:
    st.header("📊 Analyse de Marché")
    secteur = st.selectbox("Quel est votre secteur ?", ["Artisanat", "Agroalimentaire", "Tech", "Services", "Éducation"])
    region = st.text_input("Dans quelle région êtes-vous situé ?", placeholder="Ex. Tunis, Sfax, Gafsa")
    if st.button("Analyser le marché"):
        if secteur and region:
            st.success(f"📍 Analyse pour le secteur **{secteur}** à **{region}** :")
            st.write(f"""
- 💡 Demande en hausse.
- 📈 Opportunités : circuits courts, e-commerce, coopératives.
- 🚧 Risques : concurrence, fiscalité instable, accès au financement.
- ✅ Conseil : démarrez simple, testez le marché, adaptez-vous vite.
            """)
        else:
            st.warning("Veuillez indiquer secteur et région.")

# --- RECOMMANDATIONS STRATÉGIQUES ---
with tabs[3]:
    st.header("🎯 Recommandations stratégiques")
    if st.button("Obtenir des recommandations clés"):
        st.write("- Consolidez votre proposition de valeur.")
        st.write("- Étudiez votre zone de chalandise.")
        st.write("- Formalisez vos hypothèses financières.")
        st.write("- Préparez un pitch clair pour investisseurs.")

# --- FINANCES ---
with tabs[4]:
    st.header("📈 Simulation financière simplifiée")

    col1, col2 = st.columns(2)
    with col1:
        revenus_mensuels = st.number_input("💰 Revenus mensuels estimés (TND)", min_value=0, step=100)
        couts_fixes = st.number_input("🏠 Coûts fixes mensuels", min_value=0, step=50)

    with col2:
        couts_variables = st.number_input("🛒 Coûts variables mensuels", min_value=0, step=50)
        quantite_vendue = st.number_input("📦 Quantité vendue par mois", min_value=1, step=1)

    if st.button("Calculer la rentabilité"):
        cout_total = couts_fixes + couts_variables
        resultat_net = revenus_mensuels - cout_total
        cout_unitaire = cout_total / quantite_vendue if quantite_vendue > 0 else 0
        seuil_rentabilite = couts_fixes / ((revenus_mensuels / quantite_vendue) - cout_unitaire) if revenus_mensuels > cout_total else 0

        st.subheader("🔍 Résultats")
        st.write(f"💼 **Résultat net mensuel :** {resultat_net:,.2f} TND")
        st.write(f"📌 **Seuil de rentabilité :** {seuil_rentabilite:.0f} unités" if seuil_rentabilite > 0 else "⚠️ Seuil non calculable.")

        # ✅ Export PDF
        if st.button("📤 Exporter les résultats en PDF"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 14)
            pdf.cell(200, 10, "Simulation financière - EntreprendIA", ln=True, align="C")
            pdf.set_font("Arial", size=12)
            pdf.ln(10)
            pdf.cell(0, 10, f"Revenus mensuels : {revenus_mensuels} TND", ln=True)
            pdf.cell(0, 10, f"Coûts fixes : {couts_fixes} TND", ln=True)
            pdf.cell(0, 10, f"Coûts variables : {couts_variables} TND", ln=True)
            pdf.cell(0, 10, f"Quantité vendue : {quantite_vendue}", ln=True)
            pdf.cell(0, 10, f"Résultat net : {resultat_net:.2f} TND", ln=True)
            if seuil_rentabilite > 0:
                pdf.cell(0, 10, f"Seuil de rentabilité : {seuil_rentabilite:.0f} unités", ln=True)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                pdf.output(tmp_file.name)
                with open(tmp_file.name, "rb") as f:
                    st.download_button("📥 Télécharger le PDF", f, file_name="simulation_financiere.pdf")
                os.unlink(tmp_file.name)

# --- FOOTER ---
st.markdown("""
<hr>
<div style='text-align: center; color: #666;'>
⚠️ **Mode simulateur actif** – Les résultats sont fictifs pour la démonstration.
</div>
""", unsafe_allow_html=True)
