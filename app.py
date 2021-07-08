from random import choice
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='')
Bootstrap(app)

page_views = 1

@app.route('/')
def home():
    students = ['Hridaya', 'Sadhana', 'Rajaharshini', 'Priyadarshan', 'Priyam', 'Mohit', 'Sunidhi', 'Seherish',
                'Dikshith', 'Aradhana', 'Aarav', 'Siyona', 'Apparnachar', 'Nikash', 'Darshan', 'Ashwini', 'Srinidhi',
                'Aparna', 'Maya', 'Gnanedra', 'Pramita']
    if len(students) == 0:
        students.append('Hridaya', 'Sadhana', 'Rajaharshini', 'Priyadarshan', 'Priyam', 'Mohit', 'Sunidhi', 'Seherish',
                'Dikshith', 'Aradhana', 'Aarav', 'Siyona', 'Apparnachar', 'Nikash', 'Darshan', 'Ashwini', 'Srinidhi',
                'Aparna', 'Maya', 'Gnanedra', 'Pramita')
    student = choice(students)
    students.remove(student)
    global page_views
    page_views += 1
    return render_template('index.html', name=student, views=page_views)

if __name__ == "__main__":
    app.run()
