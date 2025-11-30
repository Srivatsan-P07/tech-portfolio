## 🧭 Flask Routing

In Flask, **routing** is the process of mapping a **URL path** to a specific Python function, known as a **view function**. This is done using the `@app.route()` decorator.

  * The view function defines what happens when a user navigates to that specific URL.

<!-- end list -->

```python
from flask import Flask

app = Flask(__name__)

# Basic Route: Maps the root URL '/' to the 'hello_world' function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Another Route: Maps '/about' to the 'about_page' function
@app.route('/about')
def about_page():
    return 'This is the About page.'
```

-----

## 📩 Request Handling: GET & POST

Web browsers and clients use different **HTTP methods** (or verbs) to communicate with a server. The two most common methods are **GET** and **POST**.

### 1\. GET Requests (Retrieving Data)

  * **Purpose:** Used to **request** data from a specified resource (e.g., retrieving a webpage, fetching an image).
  * **Safety & Idempotence:** **Safe** (it doesn't change the state of the server) and **Idempotent** (making the same request multiple times has the same result as making it once).
  * **Data Location:** Data (like search queries) is sent in the URL as **query strings** (e.g., `/search?q=flask`).
  * **Default:** The `@app.route()` decorator defaults to handling only `GET` requests unless specified otherwise.

### 2\. POST Requests (Submitting Data)

  * **Purpose:** Used to **submit** data to be processed to a specified resource (e.g., submitting a login form, uploading a file).
  * **Safety & Idempotence:** **Not safe** and **not idempotent** (each request might create a new resource or change server state).
  * **Data Location:** Data is sent in the **request body**, which makes it suitable for sending large amounts of data and sensitive information (like passwords).
  * **Implementation in Flask:** You must explicitly tell the route to handle `POST` requests using the `methods` argument.

<!-- end list -->

```python
from flask import request

# Route handles both GET (for initial load) and POST (for submission)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Code to handle submitted data goes here
        username = request.form['username']
        return f'Logged in as {username}'
    else:
        # Code to show the login form goes here
        return 'Show login form here (GET request)'
```

-----

## ⛓️ Route Parameters (Variable Rules)

**Route parameters** (also called variable rules) allow you to capture values specified in the URL and pass them as arguments to your view function. They are defined using angle brackets (`<...>`) in the route string.

### Basic Implementation

```python
# The value 'username' from the URL is passed as an argument to the function
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'
```

  * If a user navigates to `/user/alice`, the function returns: `User: alice`.

### Type Converters

You can specify a type for the variable rule using a converter, which helps ensure the data is of the expected type. Common converters include:

  * `string` (default): Accepts text without a slash.
  * `int`: Accepts positive integers.
  * `float`: Accepts positive floating point values.
  * `path`: Accepts strings, including slashes, which is useful for file paths.

<!-- end list -->

```python
# The 'post_id' is guaranteed to be an integer
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # post_id is now an integer, you can use it in calculations/lookups
    return f'Post ID: {post_id + 100}'
```

-----

## 📝 Form Submission

When a user submits an HTML form, the data is sent to the server. Flask uses the global `request` object to access this submitted data.

### Accessing Submitted Data

When an HTML form is submitted using the `POST` method, the data is typically encoded as `application/x-www-form-urlencoded`. Flask makes this data available through the **`request.form`** attribute, which is a dictionary-like object.

1.  **Import the `request` object:** `from flask import request`
2.  **Check the method:** Inside your view function, check if the request method is `POST`.
3.  **Access fields:** Use `request.form['field_name']` to get the value of a specific field from the submitted form data, where `'field_name'` matches the `name` attribute of the HTML input.

<!-- end list -->

```python
from flask import Flask, request, render_template

# Assume you have an HTML template 'login.html' with inputs named 'username' and 'password'

@app.route('/submit_form', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        # Retrieve data from the form
        user = request.form.get('username')  # safer way to access
        pwd = request.form['password']      # will raise an error if 'password' is missing
        
        return f'Username: {user}, Password: {pwd}'
        
    return render_template('login.html') # Renders the form on a GET request
```

-----