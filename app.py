import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter

st.set_page_config(layout="wide")

# ---------------- SESSION STATE ---------------- #
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- CUSTOM DARK UI ---------------- #
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: #e5e7eb;
    font-family: 'Segoe UI';
}
.card {
    background: rgba(30, 41, 59, 0.6);
    padding: 20px;
    border-radius: 16px;
    margin: 10px;
    border: 1px solid rgba(148,163,184,0.2);
}
.row {
    display: flex;
}
.metric {
    font-size: 26px;
    font-weight: bold;
}
.small {
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.markdown("<h1>🚀 Smart Career Navigator</h1>", unsafe_allow_html=True)

# ---------------- INPUT ---------------- #
st.subheader("Enter Your Profile")

interest = st.text_input("Interest")
skills_input = st.text_input("Skills (comma separated)")

# ---------------- CAREER DATABASE ---------------- #
career_db = {
    "Data Scientist": ["python", "data", "statistics", "ml"],
    "Backend Developer": ["java", "api", "spring"],
    "Frontend Developer": ["html", "css", "react"],
    "AI/ML Engineer": ["python", "ml", "deep learning"],
}

roadmap = {
    "Data Scientist": ["Learn Python", "Statistics", "Machine Learning", "Projects"],
    "Backend Developer": ["Learn Java", "Spring Boot", "APIs", "Projects"],
    "Frontend Developer": ["HTML/CSS", "JavaScript", "React", "Projects"],
    "AI/ML Engineer": ["Python", "ML", "DL", "Deployment"],
}

# ---------------- ANALYZE ---------------- #
if st.button("Analyze Career"):

    skills = [s.strip().lower() for s in skills_input.split(",")]

    best_match = None
    best_score = 0
    missing_skills = []

    for career, req_skills in career_db.items():
        score = len(set(skills) & set(req_skills))
        if score > best_score:
            best_score = score
            best_match = career
            missing_skills = list(set(req_skills) - set(skills))

    readiness = int((best_score / len(career_db[best_match])) * 100) if best_match else 50

    # Save history
    st.session_state.history.append(best_match)

    # ---------------- DASHBOARD ---------------- #
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f'<div class="card"><div class="small">Career</div><div class="metric">{best_match}</div></div>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div class="card"><div class="small">Readiness</div><div class="metric">{readiness}%</div></div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div class="card"><div class="small">Skills Entered</div><div class="metric">{len(skills)}</div></div>', unsafe_allow_html=True)

    # ---------------- SKILL GAP ---------------- #
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Skill Gap")
    for m in missing_skills:
        st.write("❌", m)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- ROADMAP ---------------- #
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Roadmap")
    for step in roadmap[best_match]:
        st.write("✔", step)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- CHARTS ---------------- #
    col4, col5 = st.columns(2)

    # BAR CHART
    with col4:
        st.subheader("Skill Match")
        labels = ["Matched", "Missing"]
        values = [best_score, len(missing_skills)]

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        st.pyplot(fig)

    # PIE CHART
    with col5:
        st.subheader("Readiness Distribution")
        fig2, ax2 = plt.subplots()
        ax2.pie([readiness, 100 - readiness], labels=["Ready", "Remaining"], autopct="%1.0f%%")
        st.pyplot(fig2)

# ---------------- HISTORY DASHBOARD ---------------- #
if st.session_state.history:
    st.subheader("📊 Career Recommendation History")

    counts = Counter(st.session_state.history)

    fig3, ax3 = plt.subplots()
    ax3.bar(counts.keys(), counts.values())
    st.pyplot(fig3)

# ---------------- RESET ---------------- #
if st.button("Reset"):
    st.session_state.clear()
    st.experimental_rerun()
