# 📝 Forms & User Input

Forms are the primary way users interact with your web application, submitting data like login credentials, content, or search queries. Flask handles this input through its **Request** object.

### The `request.form` Object

When a user submits a form using the **POST** method, the data is sent to the server. Flask makes this data available in the `request.form` dictionary-like object.

  * **How it works:** You access the submitted data using the **name** attribute of the HTML input field.
  * **Example Access:** If you have an input field `<input type="text" name="username">`, you access its value in Flask using `username = request.form['username']`.

### File Uploads

For file uploads (e.g., images, documents), you need two things:

1.  Set the HTML form's `enctype` to `"multipart/form-data"`.
2.  In Flask, files are stored in the `request.files` object.
      * You access the file using its input field name: `file = request.files['file_input_name']`.
      * You save the file using the file object's `save()` method: `file.save('path/to/save/filename.ext')`.

## 🛡️ Secure and Validate User Input

It's critical to **never trust user input**. All input must be validated and sanitized to prevent security vulnerabilities (like XSS or SQL injection) and ensure data integrity.

  * **Validation:** Checking if the input meets expected criteria (e.g., is an email a valid format, is a password long enough, is a required field filled out).
  * **Security:** Sanitizing data to remove malicious code before using it or storing it in a database. Flask's templating engine **Jinja2** automatically escapes most output, which is a significant security feature, but proper validation is still required on the input side.

-----

## 🛠️ Flask-WTF (Optional but Recommended)

While you can handle forms manually, **Flask-WTF** is a Flask extension that simplifies form handling, validation, and security significantly. It integrates the powerful **WTForms** library with Flask.

### Key Features of Flask-WTF:

  * **Form Definition:** You define your form fields and validators in Python classes, separating form logic from your HTML templates.
  * **Built-in Validation:** It comes with pre-built validators (required, email, length, etc.) that run server-side.
  * **CSRF Protection:** It automatically handles the **Cross-Site Request Forgery (CSRF)** token, a crucial security measure.

### The CSRF Token

**CSRF (Cross-Site Request Forgery)** is an attack where an attacker tricks a user's browser into submitting a request to an authenticated website. Flask-WTF protects against this by:

1.  Generating a unique, secret token (the **CSRF token**) when the form is displayed.
2.  Embedding this token as a hidden field in the HTML form.
3.  When the form is submitted, Flask-WTF checks if the received token matches the stored token. If they don't match, the request is rejected.

You include the token in your HTML using `{{ form.hidden_tag() }}`.

-----

## 💡 Example Implementation (with Flask-WTF)

This example shows a simple signup form implemented using Flask-WTF.

### 1\. The Python Form Definition (`forms.py`)

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# Define the form structure and validation rules
class RegistrationForm(FlaskForm):
    # Field 1: Username
    # Validator: Must be present (DataRequired) and between 2 and 20 characters
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    
    # Field 2: Email
    # Validator: Must be present and a valid email format (Email)
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    # Field 3: Password
    # Validator: Must be present and at least 6 characters
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    
    # Field 4: Submit Button
    submit = SubmitField('Sign Up')
```

### 2\. The Flask Application (`app.py`)

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RegistrationForm # Import the form we created

app = Flask(__name__)
# IMPORTANT: A secret key is required for session management and CSRF protection
app.config['SECRET_KEY'] = 'a_very_secret_and_long_string' 

@app.route('/register', methods=['GET', 'POST'])
def register():
    # 1. Create an instance of the form
    form = RegistrationForm()
    
    # 2. Server-side Validation Check
    if form.validate_on_submit():
        # If the request method is POST AND all validators pass:
        # Get the safe, validated data
        user = form.username.data
        email = form.email.data
        password = form.password.data # In a real app, hash this!
        
        # In a real application, you would save this data to a database
        print(f"User: {user}, Email: {email}, Password (Hashed): {password}")
        
        # Display a success message and redirect
        flash(f'Account created for {user}!', 'success')
        return redirect(url_for('success_page'))
    
    # 3. If GET request, or POST failed validation:
    # Render the template, passing the form object
    return render_template('register.html', title='Register', form=form)

@app.route('/success')
def success_page():
    return "Registration Successful!"

if __name__ == '__main__':
    app.run(debug=True)
```

### 3\. The HTML Template (`register.html`)

```html
<form method="POST">
    {{ form.hidden_tag() }} 
    
    <div>
        {{ form.username.label }}
        {{ form.username() }}
        
        {% for error in form.username.errors %}
            <span>[{{ error }}]</span>
        {% endfor %}
    </div>

    <div>
        {{ form.email.label }}
        {{ form.email() }}
        {% for error in form.email.errors %}
            <span>[{{ error }}]</span>
        {% endfor %}
    </div>

    <div>
        {{ form.password.label }}
        {{ form.password() }}
        {% for error in form.password.errors %}
            <span>[{{ error }}]</span>
        {% endfor %}
    </div>
    
    {{ form.submit() }}
</form>
```

-----