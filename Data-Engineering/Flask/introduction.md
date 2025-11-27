
## 💻 What is Flask?

Flask is called a "micro-framework" because it aims to keep the core simple but extensible. It provides the **essentials** for web development without forcing specific dependencies or design patterns. It does not include features like database abstraction layers, form validation, or template engines out of the box (like full-stack frameworks such as Django do), but it allows you to choose and integrate these components yourself using extensions.

It is built upon the **Werkzeug** WSGI toolkit and the **Jinja2** template engine.

-----

## ⚙️ Installing Flask

Flask is installed using Python's package installer, **pip**. It's highly recommended to use a **virtual environment** for your projects to keep dependencies separate.

### 1\. Create a Virtual Environment (Optional, but Recommended)

In your project directory:

```bash
python3 -m venv venv
```

### 2\. Activate the Virtual Environment

  * **On macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```
  * **On Windows:**
    ```bash
    venv\Scripts\activate
    ```

### 3\. Install Flask

With the environment active:

```bash
pip install Flask
```

-----

## 👋 "Hello World" App

The most basic Flask application requires only a few lines of code. Save the following in a file, for example, `app.py`:

```python
from flask import Flask

# 1. Create the Flask application instance
app = Flask(__name__)

# 2. Define a route (URL) and the function to execute when it's accessed
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# 3. Run the application
if __name__ == "__main__":
    app.run()
```

### Running the App:

1.  Make sure your virtual environment is active.
2.  Run the application from your terminal:
    ```bash
    python app.py
    ```
3.  The output will usually show the server is running at an address like `http://127.0.0.1:5000/`. Open this URL in your web browser, and you will see the message "Hello, World\!".

-----

## 🗺️ App Routes

In Flask, **routes** are used to map a specific URL to a corresponding Python function. This function's return value is what the user sees in their browser (the response). The mapping is done using the `@app.route()` **decorator**.

### Basic Routing

The example above shows the **root route**:

```python
@app.route("/") # Maps the base URL (e.g., /)
def index():
    return "This is the homepage."
```

### Routing with Variables

You can capture parts of the URL as variables to be used in your function.

```python
@app.route("/user/<username>")
def show_user_profile(username):
    # The value entered in the URL after /user/ is passed as 'username'
    return f"User: {username}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # 'int:' ensures only integer values are accepted
    return f"Post ID: {post_id}"
```

-----

## 🐛 Debug Mode

**Debug mode** is essential for development as it automatically detects changes in your code, reloads the server, and provides a powerful, interactive debugger in the browser if an error occurs.

### Enabling Debug Mode

To activate debug mode, you can pass `debug=True` to the `app.run()` method:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Alternatively, you can configure your application using environment variables before running it (recommended for modern Flask development):

1.  Set the environment variables:
      * **On macOS/Linux:**
        ```bash
        export FLASK_ENV=development
        export FLASK_APP=app.py
        ```
      * **On Windows (Command Prompt):**
        ```bash
        set FLASK_ENV=development
        set FLASK_APP=app.py
        ```
2.  Run the application using the `flask run` command:
    ```bash
    flask run
    ```

When `FLASK_ENV` is set to `development`, the debugger and reloader are enabled by default.