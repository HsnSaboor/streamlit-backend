import streamlit as st
import requests
import threading
import time
import importlib
import uvicorn

# Import the Robyn API from api.py
api_module = importlib.import_module("api")

# Function to start the Robyn API server using uvicorn
def start_api():
    uvicorn.run(api_module.app, host="127.0.0.1", port=8000)

# Start the API if it's not already running
if 'api_thread' not in st.session_state:
    api_thread = threading.Thread(target=start_api, daemon=True)
    api_thread.start()
    time.sleep(2)  # Allow some time for the server to start

API_URL = "http://localhost:8000"  # Local API URL

st.title("Simple Task Manager")

# Input to add a task
task = st.text_input("Enter a new task")

if st.button("Add Task"):
    if task:
        response = requests.post(f"{API_URL}/tasks", json={"task": task})
        if response.status_code == 200:
            st.success("Task added successfully!")
        else:
            st.error("Failed to add task.")
    else:
        st.error("Please enter a task.")

# Display existing tasks
st.subheader("Existing Tasks:")
try:
    tasks_response = requests.get(f"{API_URL}/tasks")
    tasks = tasks_response.json().get("tasks", [])
    for idx, t in enumerate(tasks):
        st.write(f"{idx + 1}. {t}")
except Exception as e:
    st.error("Failed to load tasks.")
