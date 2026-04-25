from flask import Flask, render_template, request
import joblib 
model = joblib.load("ada_model.joblib")
app = Flask(__name__)
import os
model = joblib.load(os.path.join(os.path.dirname(__file__), "ada_model.joblib"))
# Home Page
@app.route('/')
def home():
    return render_template('index.html', name="Ash")

# Student List Page
@app.route('/students')
def students():
    student_list = ["Aman", "Riya", "John"]
    return render_template('index.html', name="Students", students=student_list)

# Form Page
@app.route('/form')
def form():
    return render_template('index.html', show_form=True)

# Form Submission
@app.route('/submit', methods=['POST'])
def submit():
    values = [float(x) for x in request.form.values()]
    prediction = model.predict([values])
    return render_template('index.html', result=prediction[0])

import joblib
model = joblib.load("ada_model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    values = [float(x) for x in request.form.values()]
    prediction = model.predict([values])

    return render_template('index.html', prediction=prediction[0], values = request.form)
if __name__ == '__main__':
    app.run(debug=True)