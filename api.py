from robyn import Robyn

app = Robyn(__name__)

tasks = []  # List to hold tasks

@app.post("/tasks")
async def add_task(request):
    data = await request.json()
    task = data.get("task")
    tasks.append(task)
    return {"message": "Task added successfully!", "tasks": tasks}

@app.get("/tasks")
async def get_tasks():
    return {"tasks": tasks}

@app.get("/health")
async def health_check():
    return {"status": "API is up and running!"}

# This file does not need to run anything directly
# It will be called by Uvicorn from the main app
