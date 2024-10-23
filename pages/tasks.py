from robyn import Robyn
from flask import jsonify

app = Robyn()

@app.get("/")  # Home route
async def home():
    return "Welcome to the API!"

@app.get("/tasks")  # Tasks route
async def tasks():
    return jsonify({"message": "Tasks endpoint"})

@app.get("/data")  # Data route
async def data():
    return jsonify({"message": "Data endpoint"})

if __name__ == "__main__":
    app.run()
