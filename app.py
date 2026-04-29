import streamlit as st
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Career Navigator",
    layout="wide"
)

# ---------------- CUSTOM DARK CSS ----------------
st.markdown("""
<style>

/* Global */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0B0D17;
    color: #FFFFFF;
}

/* Headings */
h1, h2, h3 {
    font-weight: 800 !important;
    color: #FFFFFF !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #12152A;
    border-right: 1px solid #2F355F;
}

/* Cards */
.card {
    background: #1E223F;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #2F355F;
    transition: 0.3s;
}
.card:hover {
    transform: translateY(-5px);
    border-color: #6366F1;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #6366F1, #8B8FFF);
    color: white;
    border-radius: 10px;
    font-weight: 600;
    border: none;
}

/* Text */
.small-text {
    color: #C7C9D9;
    font-size: 14px;
}

.metric {
    font-size: 26px;
    font-weight: 800;
    color: #8B8FFF;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("## 🚀 Smart Career Navigator")
page = st.sidebar.radio("Navigation", ["Home", "Career Paths", "Dashboard"])

# ---------------- HOME ----------------
if page == "Home":
    st.title("Welcome back, Shruti! 👋")
    st.markdown("<div class='small-text'>Your career journey continues — keep going 🚀</div>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("<div class='card'>🎯 Career Readiness<div class='metric'>75%</div></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>✅ Skills<div class='metric'>14</div></div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'>🏆 Milestones<div class='metric'>6</div></div>", unsafe_allow_html=True)

    with col4:
        st.markdown("<div class='card'>🔥 Streak<div class='metric'>12d</div></div>", unsafe_allow_html=True)

    st.markdown("### 🎯 Target Career")
    st.markdown("""
    <div class='card'>
        🤖 <b>AI / ML Engineer</b><br>
        <span class='small-text'>Based on your profile</span><br><br>
        <b>75% Match</b>
    </div>
    """, unsafe_allow_html=True)

# ---------------- CAREER PATHS ----------------
elif page == "Career Paths":
    st.title("🧭 Career Paths")
    st.markdown("<div class='small-text'>Explore careers based on your skills</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='card'>
        ⭐ <b>AI / ML Engineer</b><br>
        <div class='small-text'>Machine learning & AI systems</div><br>
        Match: <b>75%</b>
        </div>
        """, unsafe_allow_html=True)
        st.button("Explore", key="ai")

    with col2:
        st.markdown("""
        <div class='card'>
        📊 <b>Data Analyst</b><br>
        <div class='small-text'>Data insights & visualization</div><br>
        Match: <b>68%</b>
        </div>
        """, unsafe_allow_html=True)
        st.button("Explore", key="data")

    with col3:
        st.markdown("""
        <div class='card'>
        🌐 <b>Web Developer</b><br>
        <div class='small-text'>Frontend & backend dev</div><br>
        Match: <b>55%</b>
        </div>
        """, unsafe_allow_html=True)
        st.button("Explore", key="web")

# ---------------- DASHBOARD ----------------
elif page == "Dashboard":
    st.title("📊 Progress Dashboard")

    # ---- ROW 1: BAR + PIE ----
    col1, col2 = st.columns(2)

    # BAR CHART
    with col1:
        st.subheader("Skill Levels")

        skills = ["Python", "ML", "SQL", "DL", "React"]
        values = [85, 70, 60, 45, 55]

        fig, ax = plt.subplots(figsize=(8,5))
        ax.bar(skills, values)
        ax.set_ylabel("Percentage")
        ax.set_title("Skill Progress")

        st.pyplot(fig, use_container_width=True)

    # PIE CHART
    with col2:
        st.subheader("Career Readiness")

        labels = ["Completed", "Remaining"]
        sizes = [75, 25]

        fig2, ax2 = plt.subplots(figsize=(6,5))
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax2.set_title("Overall Readiness")

        st.pyplot(fig2, use_container_width=True)

    # ---- FULL WIDTH LINE CHART ----
    st.markdown("### 📈 Weekly Learning Trend")

    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    hours = [2, 3, 1.5, 2.5, 3]

    fig3, ax3 = plt.subplots(figsize=(10,4))
    ax3.plot(days, hours, marker='o')
    ax3.set_ylabel("Hours")
    ax3.set_title("Learning Hours")

    st.pyplot(fig3, use_container_width=True)

    # ---- GOALS ----
    st.markdown("### ✅ Weekly Goals")

    st.checkbox("Complete Pandas tutorial", True)
    st.checkbox("Build ML model", True)
    st.checkbox("Practice SQL joins", False)

    # ---- ROADMAP ----
    st.markdown("### 🗺️ Roadmap")

    st.write("✔ Python Fundamentals")
    st.write("🔄 Machine Learning (In Progress)")
    st.write("⏳ Deep Learning (Upcoming)")
