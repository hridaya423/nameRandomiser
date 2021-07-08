from random import choice
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='')
Bootstrap(app)

@app.route('/')
def home():
    page_views = 1
    students = ['Hridaya', 'Sadhana', 'Rajaharshini', 'Priyadarshan', 'Priyam', 'Mohit', 'Sunidhi', 'Seherish',
                'Dikshith', 'Aradhana', 'Aarav', 'Siyona', 'Apparnachar', 'Nikash', 'Darshan', 'Ashwini', 'Srinidhi',
                'Aparna', 'Maya', 'Gnanedra', 'Pramita']
    page_views += 1
    return render_template('index.html', name=choice(students), views=page_views)

if __name__ == "__main__":
    app.run()
