from flask import Flask, render_template, request
import mysql.connector
import config

app = Flask(__name__)

def db_connection():
    return mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )

def init_db():
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add')
def add_feedback():
    return render_template('add_feedback.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        conn = db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO feedback (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return "Feedback stored successfully"

    except mysql.connector.Error as err:
        return f"Database Error: {err}"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    init_db()
    app.run(debug=config.DEBUG)