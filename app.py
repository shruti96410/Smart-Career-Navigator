from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'secret123'


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


# ---------------- ROUTES ---------------- #

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/signup')
def signup_page():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users VALUES (NULL, ?, ?)", (username, password))
        conn.commit()
    except:
        return "User already exists"
    finally:
        conn.close()

    return redirect(url_for('home'))


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Admin login
    if username == 'admin' and password == 'admin':
        session['admin'] = True
        return redirect(url_for('admin'))

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()

    if user and password == user[0]:
        session['user'] = username
        return render_template('index.html')
    else:
        return "Invalid credentials"


@app.route('/admin')
def admin():
    if 'admin' not in session:
        return redirect(url_for('home'))

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT username FROM users")
    users = c.fetchall()
    conn.close()

    return render_template('admin.html', users=users, total=len(users))


# ---------------- CAREER PREDICTION ---------------- #

@app.route('/predict', methods=['POST'])
def predict():
    interest = request.form.get('interest')
    skills = request.form.get('skills')

    if 'code' in skills.lower():
        result = 'Software Developer'
    elif 'design' in interest.lower():
        result = 'UI/UX Designer'
    elif 'data' in skills.lower():
        result = 'Data Scientist'
    else:
        result = 'Explore Multiple Fields'

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
            "desc": "Explore domains to find your path.",
            "skills": "Basic Programming",
            "link": "https://roadmap.sh"
        }
    }

    info = career_info.get(result)

    explanation = f"Based on your interest '{interest}' and skills '{skills}', this career suits you."

    required_skills = {
        "Software Developer": ["python", "dsa", "html"],
        "UI/UX Designer": ["figma", "design"],
        "Data Scientist": ["python", "ml"]
    }

    user_skills = skills.lower().split()
    missing = [s for s in required_skills.get(result, []) if s not in user_skills]

    roadmap = {
        "Software Developer": "Python → DSA → Projects",
        "UI/UX Designer": "Figma → UX → Portfolio",
        "Data Scientist": "Python → Statistics → ML"
    }

    return render_template(
        'result.html',
        result=result,
        info=info,
        explanation=explanation,
        missing=missing,
        roadmap=roadmap.get(result)
    )


# ---------------- CHATBOT ---------------- #

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_msg = request.form.get('message').lower()

    if "career" in user_msg:
        reply = "You can explore Software Development, Data Science, or UI/UX based on your skills."
    elif "data" in user_msg:
        reply = "For Data Science, learn Python, Statistics, and Machine Learning."
    elif "developer" in user_msg:
        reply = "For Software Developer, learn Python, DSA, and Web Development."
    elif "design" in user_msg:
        reply = "For UI/UX, learn Figma and design principles."
    else:
        reply = "Ask me about careers, skills, or learning paths!"

    return {"response": reply}


# ---------------- LOGOUT ---------------- #

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


# ---------------- RUN APP ---------------- #

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
