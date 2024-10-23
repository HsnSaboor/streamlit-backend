from robyn import Robyn, jsonify

app = Robyn(__file__)

@app.get("/")
async def home(request):
    return "Welcome to the API!"

@app.route('/tasks')  # Renamed route to /tasks
def tasks():
    # Your tasks logic
    return jsonify({"message": "Tasks endpoint"})

if __name__ == "__main__":
    app.start(port=8080, host="0.0.0.0")
