from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


# Примерен речник с потребители
users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
}


@app.route('/')
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = request.args.get('name', 'Plamena')
    return render_template('index.html', title='Home Page', name=name, current_time=current_time, users=users)


@app.route('/form')
def form():
    return render_template('form.html', title='Form Page')


@app.route('/all-users')
def all_users():
    return render_template('all_users.html', title='All Users', users=users)


@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', title='Greet Page', name=name)


if __name__ == '__main__':
    app.run(debug=True)
