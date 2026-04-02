
import streamlit as st
import sqlite3

# ---------------- DATABASE ---------------- #
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ---------------- AUTH ---------------- #

def signup(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users VALUES (NULL, ?, ?)", (username, password))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def login(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()

    if user and password == user[0]:
        return True
    return False


# ---------------- SESSION ---------------- #
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ---------------- UI ---------------- #

st.title("🚀 Smart Career Navigator")

menu = ["Login", "Signup"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- SIGNUP ---------------- #
if choice == "Signup":
    st.subheader("Create Account")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Signup"):
        if signup(user, pwd):
            st.success("Account created successfully!")
        else:
            st.error("User already exists")

# ---------------- LOGIN ---------------- #
elif choice == "Login":
    st.subheader("Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(user, pwd):
            st.session_state.logged_in = True
            st.session_state.username = user
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

# ---------------- MAIN APP ---------------- #
if st.session_state.logged_in:

    st.subheader(f"Welcome, {st.session_state.username}")

    interest = st.text_input("Enter your interests")
    skills = st.text_input("Enter your skills")

    if st.button("Find My Career"):

        if "code" in skills.lower():
            result = "Software Developer"
        elif "design" in interest.lower():
            result = "UI/UX Designer"
        elif "data" in skills.lower():
            result = "Data Scientist"
        else:
            result = "Explore Multiple Fields"

        st.success(f"🎯 Recommended Career: {result}")

        career_info = {
            "Software Developer": {
                "desc": "Builds applications and systems.",
                "skills": "Python, Java, DSA, Web Dev",
                "link": "https://roadmap.sh/software-engineer"
            },
            "UI/UX Designer": {
                "desc": "Designs user-friendly interfaces.",
                "skills": "Figma, UX, Creativity",
                "link": "https://roadmap.sh/design"
            },
            "Data Scientist": {
                "desc": "Analyzes data and builds models.",
                "skills": "Python, ML, SQL",
                "link": "https://roadmap.sh/data-scientist"
            },
            "Explore Multiple Fields": {
                "desc": "Explore domains.",
                "skills": "Basic Programming",
                "link": "https://roadmap.sh"
            }
        }

        info = career_info.get(result)

        st.write(f"📘 {info['desc']}")
        st.write(f"🛠 Required Skills: {info['skills']}")
        st.markdown(f"[🔗 View Roadmap]({info['link']})")

        # Skill gap
        required_skills = {
            "Software Developer": ["python", "dsa", "html"],
            "UI/UX Designer": ["figma", "design"],
            "Data Scientist": ["python", "ml"]
        }

        user_skills = skills.lower().split()
        missing = [s for s in required_skills.get(result, []) if s not in user_skills]

        if missing:
            st.warning(f"⚠ Missing Skills: {', '.join(missing)}")

    # ---------------- CHATBOT ---------------- #
    st.subheader("💬 Chatbot")

    msg = st.text_input("Ask something...")

    if st.button("Send"):
        if "career" in msg.lower():
            st.write("Explore Software Dev, Data Science, or UI/UX.")
        elif "data" in msg.lower():
            st.write("Learn Python, Statistics, and ML.")
        elif "developer" in msg.lower():
            st.write("Learn Python, DSA, Web Dev.")
        elif "design" in msg.lower():
            st.write("Learn Figma and UX.")
        else:
            st.write("Ask about careers or skills!")

    # ---------------- LOGOUT ---------------- #
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.experimental_rerun()
