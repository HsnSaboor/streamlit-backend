from robyn import Robyn

app = Robyn(__name__)

tasks = []  # This will hold our tasks

@app.post("/tasks")
async def add_task(task: str):
    tasks.append(task)
    return {"message": "Task added successfully!", "tasks": tasks}

@app.get("/tasks")
async def get_tasks():
    return {"tasks": tasks}

@app.get("/health")
async def health_check():
    return {"status": "API is up and running!"}

# You don't run the app here; it will be run from an ASGI server instead
