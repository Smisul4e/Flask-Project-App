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
    name = request.args.get('name', 'Guest')
    return render_template('index.html', title='Home Page', name=name, current_time=current_time, users=users)

@app.route('/form')
def form():
    return render_template('form.html', title='Form Page')

@app.route('/all-users')
def all_users():
    return render_template('all_users.html', title='All Users', users=users)

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', title='Greet', user=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return f"User: {username}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Subpath {subpath}"

@app.route('/item/<int:item_id>')
def show_item(item_id):
    return render_template('item.html', title='Item', item_id=item_id)

@app.route('/greet', methods=['GET'])
def greet_query():
    name = request.args.get('name', 'Guest')
    return f"Hello, {name}!"

@app.route('/update_profile', methods=['POST'])
def update_profile():
    username = request.form['username']
    email = request.form['email']
    return f"Updating profile of {username} with email {email}"

@app.route('/update-profile-form')
def update_profile_form():
    return render_template('update_profile.html', title='Update Profile')

# Нов маршрут за актуализиране на страната на потребител
@app.route('/update-country', methods=['GET', 'POST'])
def update_country():
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        if name in users:
            users[name]['country'] = country
            message = f"Updated {name}'s country to {country}."
        else:
            users[name] = {'age': 0, 'country': country}
            message = f"Added new user {name} with country {country}."
        return render_template('update_country.html', title='Update Country', message=message)
    return render_template('update_country.html', title='Update Country')

if __name__ == '__main__':
    app.run(debug=True)
