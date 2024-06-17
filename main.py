from flask import Flask, render_template, request, redirect, url_for
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
    name = request.args.get('name', 'Guest')
    return f"Welcome to the home page, {name}! Current time: {current_time}"

@app.route('/update-country', methods=['GET', 'POST'])
def update_country():
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        if name in users:
            users[name]['country'] = country
            return redirect(url_for('all_users'))  # Redirect to the all_users route
        else:
            return f"User {name} not found."
    return '''
        <form method="post">
            <label for="name">Username:</label><br>
            <input type="text" id="name" name="name"><br><br>
            <label for="country">New Country:</label><br>
            <input type="text" id="country" name="country"><br><br>
            <input type="submit" value="Update Country">
        </form>
    '''

@app.route('/all-users')
def all_users():
    return render_template('all_users.html', title='All Users', users=users)

if __name__ == '__main__':
    app.run(debug=True)
