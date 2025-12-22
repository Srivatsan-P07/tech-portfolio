from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    #User Details
    user_name = "John Doe"
    account_balance = 2500.00
    is_premium_member = True

    notifications = ["New login detected", "Invoice paid", "Profile updated"]
    settings = {
        "theme": "dark",
        "notifications_enabled": True,
        "language": "EN"
    }
    print(json.dumps(notifications))

    return render_template(
        'index.html',
        user_name = user_name,
        account_balance = account_balance,
        is_premium_member = is_premium_member,
        
        # Notification
        notifications = json.dumps(notifications),
        settings = json.dumps(settings)
    )

if __name__ == '__main__':
    app.run(debug=True)