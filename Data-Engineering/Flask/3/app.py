from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Simple validation
        if username == 'admin' and password == 'secret':
            return redirect(url_for('success', user=username))

    else:
        error = 'Invalid Credentials. Please try again.'
    
    return render_template('index.html', error=error)

@app.route('/success/<user>')
def success(user):
    return f'<h1>Login Successful!</h1><p>Welcome, {user}!</p>'

if __name__ == '__main__':
    app.run(debug=True)
