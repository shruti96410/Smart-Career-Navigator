import streamlit as st
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart Career Navigator", layout="wide")

# ---------------- SESSION STATE ----------------
if "selected_career" not in st.session_state:
    st.session_state.selected_career = None

# ---------------- DARK THEME CSS ----------------
st.markdown("""
<style>

/* Global Dark Theme */
html, body, [class*="css"] {
    background-color: #0B0D17 !important;
    color: #E8EAF6 !important;
    font-family: 'DM Sans', sans-serif;
}

/* Force readable text */
* {
    color: #E8EAF6 !important;
}

/* Headings */
h1, h2, h3 {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #12152A !important;
}

/* Cards */
.card {
    background: #1E223F;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #2F355F;
    margin-bottom: 15px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #6366F1, #8B8FFF);
    color: white !important;
    font-weight: 700;
    border-radius: 10px;
    border: none;
}

/* Labels */
label {
    color: #E8EAF6 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🚀 Smart Career Navigator")
page = st.sidebar.radio("Navigation", ["Home", "Career Paths", "Dashboard"])

# ---------------- HOME ----------------
if page == "Home":
    st.title("Welcome back, Shruti! 👋")
    st.write("Your career journey continues — keep going 🚀")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("<div class='card'><b>🎯 Career Readiness</b><br><h2>75%</h2></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'><b>✅ Skills</b><br><h2>14</h2></div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'><b>🏆 Milestones</b><br><h2>6</h2></div>", unsafe_allow_html=True)

    with col4:
        st.markdown("<div class='card'><b>🔥 Streak</b><br><h2>12d</h2></div>", unsafe_allow_html=True)

    st.markdown("### 🎯 Target Career")
    st.markdown("""
    <div class='card'>
        🤖 <b>AI / ML Engineer</b><br><br>
        <b>75% Match</b>
    </div>
    """, unsafe_allow_html=True)

# ---------------- CAREER PATHS ----------------
elif page == "Career Paths":
    st.title("🧭 Career Paths")
    st.write("Explore careers based on your skills")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'><b>🤖 AI / ML Engineer</b><br>Match: 75%</div>", unsafe_allow_html=True)
        if st.button("Explore AI/ML"):
            st.session_state.selected_career = "AI"

    with col2:
        st.markdown("<div class='card'><b>📊 Data Analyst</b><br>Match: 68%</div>", unsafe_allow_html=True)
        if st.button("Explore Data"):
            st.session_state.selected_career = "Data"

    with col3:
        st.markdown("<div class='card'><b>🌐 Web Developer</b><br>Match: 55%</div>", unsafe_allow_html=True)
        if st.button("Explore Web"):
            st.session_state.selected_career = "Web"

# ---------------- CAREER DETAILS ----------------
if st.session_state.selected_career:

    st.markdown("## 🚀 Career Details")

    if st.session_state.selected_career == "AI":
        st.markdown("""
        ### 🤖 AI / ML Engineer
        **Skills Required:**
        - Python
        - Machine Learning
        - Deep Learning

        **Tools:**
        - TensorFlow
        - Scikit-learn

        **Roadmap:**
        1. Learn Python
        2. Learn ML Algorithms
        3. Work on Projects
        """)

    elif st.session_state.selected_career == "Data":
        st.markdown("""
        ### 📊 Data Analyst
        **Skills Required:**
        - SQL
        - Excel
        - Python

        **Tools:**
        - Power BI
        - Tableau
        """)

    elif st.session_state.selected_career == "Web":
        st.markdown("""
        ### 🌐 Web Developer
        **Skills Required:**
        - HTML, CSS, JavaScript

        **Frameworks:**
        - React
        - Node.js
        """)

    if st.button("⬅ Back"):
        st.session_state.selected_career = None

# ---------------- DASHBOARD ----------------
elif page == "Dashboard":
    st.title("📊 Progress Dashboard")

    col1, col2 = st.columns(2)

    # BAR CHART
    with col1:
        skills = ["Python", "ML", "SQL", "DL", "React"]
        values = [85, 70, 60, 45, 55]

        fig, ax = plt.subplots(figsize=(8,5))
        ax.bar(skills, values)
        ax.set_title("Skill Progress")
        ax.set_ylabel("Percentage")

        st.pyplot(fig, use_container_width=True)

    # PIE CHART
    with col2:
        labels = ["Completed", "Remaining"]
        sizes = [75, 25]

        fig2, ax2 = plt.subplots(figsize=(6,5))
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax2.set_title("Career Readiness")

        st.pyplot(fig2, use_container_width=True)

    # LINE CHART
    st.markdown("### 📈 Weekly Learning")

    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    hours = [2, 3, 1.5, 2.5, 3]

    fig3, ax3 = plt.subplots(figsize=(10,4))
    ax3.plot(days, hours, marker='o')
    ax3.set_title("Learning Hours")

    st.pyplot(fig3, use_container_width=True)

    # GOALS
    st.markdown("### ✅ Weekly Goals")
    st.checkbox("Complete Pandas tutorial", True)
    st.checkbox("Build ML model", True)
    st.checkbox("Practice SQL joins", False)
