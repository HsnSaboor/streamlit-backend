from robyn import Robyn

app = Robyn(__name__)

# In-memory task storage (for simplicity)
tasks = []

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def add_task(task: str):
    tasks.append(task)
    return {"message": "Task added", "tasks": tasks}

if __name__ == "__main__":
    app.run()
