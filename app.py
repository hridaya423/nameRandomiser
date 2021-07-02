from random import choice
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='')
Bootstrap(app)


@app.route('/')
def home():
    students = ['Hridaya', 'Sadhana', 'Rajaharshini', 'Priyadarshan', 'Priyam', 'Mohit', 'Sunidhi', 'Seherish',
                'Dikshith', 'Aradhana', 'Aarav', 'Siyona', 'Apparnachar', 'Nikash', 'Darshan', 'Ashwini', 'Srinidhi',
                'Aparna', 'Maya', 'Gnanedra', 'Pramita']
    return render_template('index.html', name=choice(students))


app.run()
