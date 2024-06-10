from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
}


@app.route('/')
def home():
    name = request.args.get('name', 'Alice')
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', title='Home Page', name=name, current_time=current_time, users=users)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/all-users')
def all_users():
    return render_template('all_users.html', title='All Users', users=users)


if __name__ == '__main__':
    app.run(debug=True)
