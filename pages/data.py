# If using Flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')  # Separate route for data if needed
def data():
    # Your data logic
    return jsonify({"message": "Data endpoint"})
