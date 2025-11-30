from flask import Flask, render_template

app = Flask(__name__)

USERS = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example'}
]

@app.route('/')
def index():
    return render_template(
        'index.html',
        page_title='User List Jinja2',
        users=USERS,
        is_admin=True
    )

if __name__ == '__main__':
    app.run(debug=True)