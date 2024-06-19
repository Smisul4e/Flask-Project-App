import logging
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Logging configuration
logging.basicConfig(level=logging.DEBUG)

# Sample dictionary of users
users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
}

@app.route('/')
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = request.args.get('name', 'Guest')
    return render_template('index.html', title='Home Page', name=name, current_time=current_time)

@app.route('/all-users')
def all_users():
    return render_template('all_users.html', title='All Users', users=users)

@app.route('/update-country', methods=['GET', 'POST'])
def update_country():
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        if name in users:
            users[name]['country'] = country
            return redirect(url_for('all_users'))
        else:
            return f"User {name} not found."
    return render_template('update_country.html', title='Update Country')

# Custom error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404 - Page Not Found 😞'), 404

if __name__ == '__main__':
    app.run(debug=True)
