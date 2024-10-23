# app.py
from robyn import Robyn, jsonify, Response

app = Robyn(__file__)

# Example route for greeting
@app.get("/greet")
async def greet(request):
    return jsonify({"message": "Hello, world!"})

# Endpoint to get a task by ID
@app.get("/task/<id>")
async def get_task(request, path_params):
    task_id = path_params["id"]
    # Here you would normally retrieve the task from a database or other storage
    return jsonify({"id": task_id, "name": f"Task {task_id}", "status": "pending"})

# Endpoint to create a new task
@app.post("/task")
async def create_task(request):
    task_data = await request.json()  # Get JSON body from request
    # Here you would normally save the task to a database
    return Response(status_code=201, description="Task created")

# Starting the server
if __name__ == "__main__":
    app.start(port=8080, host="0.0.0.0")
