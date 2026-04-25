from flask import Flask, render_template, request, redirect
import sqlite3
import joblib

app = Flask(__name__)

# Load ML Mod
import os
model_path = os.path.join(os.path.dirname(__file__), "ada_model.joblib")
model = joblib.load(model_path)

# Initialize DB
def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            marks INTEGER
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Home
@app.route('/')
def home():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template('index.html', students=students)


# Add Student
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    marks = int(request.form['marks'])

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
    conn.commit()
    conn.close()

    return redirect('/')


# Delete
@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect('/')


# Predict (ML Integration)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        values = [
            float(request.form['f1']),
            float(request.form['f2']),
            float(request.form['f3']),
            float(request.form['f4']),
            float(request.form['f5']),
            float(request.form['f6']),
            float(request.form['f7']),
            float(request.form['f8']),
            float(request.form['f9']),
            float(request.form['f10'])
        ]

        prediction = model.predict([values])[0]

        return render_template('index.html',
                               prediction=prediction,
                               values=request.form)

    except Exception as e:
        return f"Error: {e}"
    

if __name__ == '__main__':
    app.run(debug=True)