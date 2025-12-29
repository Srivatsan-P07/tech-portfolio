from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    updates = {
        "title": "Dynamic Title " + str(random.randint(1, 100)),
        "image_url": "https://picsum.photos/200/300?random=" + str(random.randint(1,100)),
        "link": "https://google.com",
        "color": random.choice(["#3498db", "#e74c3c", "#2ecc71", "#f1c40f"])
    }
    return jsonify(updates)

if __name__ == '__main__':
    app.run(debug=True)