# Folder Structure

```
/my_flask_app
    ├── app.py
    ├── static/
    │   └── script.js
    └── templates/
        └── index.html
```
### 1. The Python Backend (`app.py`)

This file handles the routing and prepares various data types (strings, booleans, lists, and dictionaries) to be sent to the frontend.

```python
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    # 2. Variables & Data Types
    user_name = "Alex Archer"
    account_balance = 1250.50
    
    # 3. Control Flow Logic
    is_premium_member = True
    
    # 5. Data Structures
    notifications = ["New login detected", "Invoice paid", "Profile updated"]
    settings = {
        "theme": "dark",
        "notifications_enabled": True,
        "language": "EN"
    }
    
    return render_template(
        'index.html', 
        name=user_name, 
        balance=account_balance,
        is_premium=is_premium_member,
        notifications=notifications,
        settings=settings
    )

if __name__ == '__main__':
    app.run(debug=True)

```

---

### 2. The HTML Template (`templates/index.html`)

This file uses **Jinja2** syntax (the `{{ }}` and `{% %}` blocks) to bridge Python data into JavaScript.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask + JS Integration</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

    <h1>Welcome, {{ name }}</h1>

    <div id="dashboard">
        {% if is_premium %}
            <p style="color: gold;">⭐ Premium Member Status Active</p>
        {% else %}
            <p><a href="/upgrade">Upgrade to Premium</a></p>
        {% endif %}
    </div>

    <button onclick="checkBalance('{{ name }}', {{ balance }})">
        Check Balance
    </button>

    <script src="script.js"></script>
</body>
</html>

```

### 3. Javascript Code

```js
// 2. Variables & Data Types: Injecting Python values into JS
const userName = "{{ name }}";
const balance = {{ balance }};

// 4. Functions: Logic to interact with Flask-provided data
function checkBalance(user, amount) {
    alert(`User: ${user}\nAvailable Balance: $${amount.toFixed(2)}`);
}

// 5. Data Structures: Converting Python List/Dict to JS JSON
const userNotifications = {{ notifications | tojson }};
const userSettings = {{ settings | tojson }};

console.log("Loading Notifications...");
userNotifications.forEach((note, index) => {
    console.log(`${index + 1}: ${note}`);
});

console.log("Current Theme:", userSettings.theme);

// 3. Control Flow in JS: Deciding logic based on Flask variables
if (userSettings.theme === "dark") {
    document.body.style.backgroundColor = "#2c3e50";
    document.body.style.color = "white";
}
```

### Key Takeaways for Integration

| Concept | Python Side | JS/HTML Side (Jinja2) |
| --- | --- | --- |
| **Static Files** | `app = Flask(__name__)` | `url_for('static', filename='...')` |
| **Simple Data** | `val = "Hello"` | `const jsVal = "{{ val }}";` |
| **Logic** | `if user.active:` | `{% if user_active %} ... {% endif %}` |
| **Complex Data** | `my_dict = {"a": 1}` | `const data = {{ my_dict | tojson }};` |

### Next Steps

To run this, ensure you have Flask installed (`pip install flask`), save the code above into their respective files, and run `python app.py`.