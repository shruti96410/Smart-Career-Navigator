import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# ---------------- DARK THEME ---------------- #
st.markdown("""
<style>
body {background-color:#0D0F1A; color:white;}
.block-container {padding: 2rem;}
.card {
    background:#181C34;
    padding:20px;
    border-radius:16px;
    border:1px solid #252A47;
}
.title {
    font-size:26px;
    font-weight:800;
}
.metric {
    font-size:28px;
    font-weight:700;
}
.small {color:#9CA3AF; font-size:13px;}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("🚀 Smart Career Navigator")
menu = st.sidebar.radio("Menu", ["Dashboard", "Career"])

# ---------------- DASHBOARD ---------------- #
if menu == "Dashboard":

    # TOPBAR
    col1, col2 = st.columns([6,2])
    col1.markdown('<div class="title">Progress Dashboard</div>', unsafe_allow_html=True)
    col2.write("📅 April 2026")

    st.markdown("---")

    # ---------------- STAT CARDS ---------------- #
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown('<div class="card"><div class="small">Career Readiness</div><div class="metric">75%</div></div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="card"><div class="small">Skills Acquired</div><div class="metric">14</div></div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="card"><div class="small">Milestones</div><div class="metric">6</div></div>', unsafe_allow_html=True)

    with c4:
        st.markdown('<div class="card"><div class="small">Learning Streak</div><div class="metric">12d</div></div>', unsafe_allow_html=True)

    st.markdown("###")

    # ---------------- MID SECTION ---------------- #
    left, right = st.columns([2,1])

    # SKILLS
    with left:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Skill Completion Tracker")

        skills = {
            "Python":85,
            "Machine Learning":70,
            "SQL":60,
            "Deep Learning":45,
            "React":55,
            "NLP":30
        }

        for skill, val in skills.items():
            st.write(skill)
            st.progress(val)

        st.markdown('</div>', unsafe_allow_html=True)

    # CIRCLE (SIMULATED)
    with right:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Overall Readiness")

        fig, ax = plt.subplots()
        ax.pie([75,25], labels=["",""], autopct='%1.0f%%')
        st.pyplot(fig)

        st.write("AI/ML Engineer")
        st.caption("Target Role Match")

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("###")

    # ---------------- BOTTOM ---------------- #
    left2, right2 = st.columns(2)

    # ROADMAP
    with left2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Next Roadmap Steps")

        st.write("✔ Python Fundamentals (Done)")
        st.write("🔵 ML Algorithms (Active)")
        st.write("⚪ Deep Learning (Pending)")
        st.write("⚪ NLP Models (Pending)")

        st.markdown('</div>', unsafe_allow_html=True)

    # GOALS + MILESTONES
    with right2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Weekly Goals")

        st.write("✔ Pandas tutorial (Mon)")
        st.write("✔ Linear regression (Tue)")
        st.write("✔ Neural networks (Wed)")
        st.write("⬜ SQL practice (Thu)")
        st.write("⬜ GitHub project (Fri)")

        st.subheader("Milestones")
        st.write("🚀 First Step")
        st.write("🔥 7-Day Streak")
        st.write("🧠 ML Learner")
        st.write("🏅 Deep Diver (Locked)")

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CAREER PAGE ---------------- #
elif menu == "Career":
    st.title("Career Recommendation")

    interest = st.text_input("Interest")
    skills = st.text_input("Skills (comma separated)")

    if st.button("Analyze"):
        st.success("Recommended: Data Scientist")
        st.info("Based on your skills")
        st.warning("Missing: Machine Learning")

        st.progress(60)
