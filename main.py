import streamlit as st

# Fonction simulée pour tester sans clé API
def ask_gpt(prompt):
    return f"\n💬 **Réponse simulée :** Vous avez demandé : _{prompt}_\n"

# Configuration de la page
st.set_page_config(page_title="EntreprendIA – Prototype IA pour Entrepreneurs", layout="wide")

# Bandeau principal
st.markdown("""
<div style='text-align: center;'>
    <h1 style='font-size:3em;'>🚀 EntreprendIA</h1>
    <h2 style='color: grey;'>Prototype IA pour un accompagnement entrepreneurial innovant</h2>
    <p style='font-size:1.1em;'>Explorez les fonctionnalités en mode simulateur avant le déploiement complet. Bientôt, des conseils enrichis par des sources nationales et internationales, adaptés aux profils et secteurs.</p>
</div>
<hr>
""", unsafe_allow_html=True)

# Sidebar enrichie
st.sidebar.title("🔧 Navigation & Améliorations")
st.sidebar.info("💡 Passez en mode API pour des réponses réelles et connectées à OpenAI et à des bases sectorielles et nationales.")
st.sidebar.markdown("""
**Améliorations prévues :**
- 🔹 Historique des sessions & suivis
- 🔹 Profils utilisateurs avec préférences
- 🔹 Connexion à des bases nationales (INS, APII) et internationales (OECD, Eurostat)
- 🔹 Moteur de recommandations IA inspiré de GrowthBar, Jasper AI
- 🔹 Rapports téléchargeables en PDF/Excel
- 🔹 Tableaux de bord interactifs et comparatifs sectoriels
- 🔹 Génération automatisée de plans d’affaires détaillés par secteur
""")

st.sidebar.markdown("""
**Feuille de route :**
1️⃣ Connexion API sécurisée<br>
2️⃣ Personnalisation par secteur et profil<br>
3️⃣ Intégration de bases de données nationales et internationales<br>
4️⃣ Module prédictif (machine learning, benchmarks)<br>
5️⃣ Monétisation (abonnements, crédits, partenariats)
""", unsafe_allow_html=True)

# Onglets principaux
st.markdown("### 🗂️ Modules disponibles")
tabs = st.tabs(["🤖 Assistance", "💡 Idées", "📊 Analyse Marché", "🗺️ Géomarketing", "📈 Simulation financière", "📝 Plan d'affaire complet"])

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
        analysis = ask_gpt(f"Analyse marché enrichie par les sources locales et internationales pour : {secteur_analyse}")
        st.success(analysis)

with tabs[3]:
    st.subheader("Géomarketing & zone de chalandise")
    zone = st.text_input("Zone géographique (ville ou région) :", placeholder="Ex. Tunis, Sfax")
    if st.button("Analyser la zone", key="btn4") and zone:
        geo_analysis = ask_gpt(f"Analyse géomarketing avec données enrichies pour : {zone}")
        st.success(geo_analysis)

with tabs[4]:
    st.subheader("Simulation financière")
    projet = st.text_input("Type de projet :", placeholder="Ex. Café, start-up tech")
    if st.button("Simuler les finances", key="btn5") and projet:
        finance = ask_gpt(f"Simulation financière détaillée pour : {projet}")
        st.success(finance)

with tabs[5]:
    st.subheader("Plan d'affaire complet")
    projet_nom = st.text_input("Nom du projet :", placeholder="Ex. Mon Café Innovant")
    if st.button("Générer le plan d'affaire", key="btn6") and projet_nom:
        business_plan = ask_gpt(f"Génère un plan d'affaire structuré pour : {projet_nom} comprenant résumé exécutif, étude de marché, stratégie, prévisions financières, besoins d'investissement et indicateurs clés.")
        st.success(business_plan)

st.markdown("""
<hr>
<div style='text-align: center; color: grey;'>
    ⚠️ **Note :** Mode simulateur activé. Les réponses affichées sont fictives et servent à la démonstration. Pour débloquer les fonctionnalités avancées, connectez une clé API OpenAI et activez l'accès aux bases spécialisées et externes.
</div>
""", unsafe_allow_html=True)
