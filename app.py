import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart Career Navigator", layout="wide")

# ---------------- CUSTOM CSS (DARK UI) ----------------
st.markdown("""
<style>
body {
    background-color: #0D0F1A;
    color: #E8EAF6;
}

.sidebar .sidebar-content {
    background-color: #13162A;
}

h1, h2, h3 {
    color: #E8EAF6;
    font-weight: 800;
}

.card {
    background: #181C34;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #252A47;
    margin-bottom: 15px;
}

.metric {
    font-size: 28px;
    font-weight: bold;
}

.tag {
    background: #252A47;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 12px;
    margin-right: 5px;
}

.button-primary {
    background: #6366F1;
    color: white;
    padding: 8px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("## 🚀 Smart Career Navigator")
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🧭 Career Paths", "📊 Dashboard"]
)

# ---------------- HOME PAGE ----------------
if page == "🏠 Home":

    st.markdown("## 👋 Welcome back, Shruti!")
    st.caption("Your career journey continues — keep going!")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="card"><div class="metric">75%</div>Career Readiness</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><div class="metric">14</div>Skills Acquired</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card"><div class="metric">6</div>Milestones</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="card"><div class="metric">12d</div>Streak</div>', unsafe_allow_html=True)

    st.markdown("### 🎯 Target Career")
    st.markdown("""
    <div class="card">
        <h3>🤖 AI / ML Engineer</h3>
        <p>Based on your profile and interests</p>
        <b>Match: 75%</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📌 Today's Tasks")
    st.markdown("""
    <div class="card">📚 Continue Machine Learning Module (45 min)</div>
    <div class="card">🧪 Practice SQL Joins (30 min)</div>
    <div class="card">📝 Submit Mini Project (1 hr)</div>
    """, unsafe_allow_html=True)


# ---------------- CAREER PATHS ----------------
elif page == "🧭 Career Paths":

    st.markdown("## 🧭 Career Paths")
    st.caption("Explore careers matched to your skills")

    col1, col2, col3 = st.columns(3)

    def career_card(title, desc, match, skills):
        st.markdown(f"""
        <div class="card">
            <h3>{title}</h3>
            <p>{desc}</p>
            <b>Match: {match}%</b><br><br>
            {" ".join([f'<span class="tag">{s}</span>' for s in skills])}
        </div>
        """, unsafe_allow_html=True)

    with col1:
        career_card("🤖 AI/ML Engineer",
                    "Build intelligent systems",
                    75,
                    ["Python", "ML", "NLP"])

    with col2:
        career_card("📊 Data Analyst",
                    "Analyze and visualize data",
                    68,
                    ["SQL", "Excel", "Power BI"])

    with col3:
        career_card("🌐 Web Developer",
                    "Build web applications",
                    55,
                    ["HTML", "JS", "React"])

    col4, col5, col6 = st.columns(3)

    with col4:
        career_card("🔐 Cybersecurity",
                    "Secure systems",
                    45,
                    ["Linux", "Networking"])

    with col5:
        career_card("☁️ Cloud Engineer",
                    "Manage cloud infra",
                    50,
                    ["AWS", "Docker"])

    with col6:
        career_card("📱 App Developer",
                    "Build mobile apps",
                    40,
                    ["Flutter", "Java"])


# ---------------- DASHBOARD ----------------
elif page == "📊 Dashboard":

    st.markdown("## 📊 Progress Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📈 Skill Progress")
        st.progress(85)
        st.write("Python")

        st.progress(70)
        st.write("Machine Learning")

        st.progress(60)
        st.write("SQL")

        st.progress(45)
        st.write("Deep Learning")

    with col2:
        st.markdown("### 🎯 Readiness")
        st.metric(label="Career Readiness", value="75%")

    st.markdown("### 🗺️ Roadmap")
    st.markdown("""
    - ✅ Python Fundamentals  
    - 🔄 ML Algorithms  
    - ⏳ Deep Learning  
    - ⏳ NLP  
    """)

    st.markdown("### 🏆 Milestones")
    st.markdown("""
    🚀 First Step  
    🔥 7-Day Streak  
    🧠 ML Learner  
    """)
