import streamlit as st
import requests
import threading
import time
import importlib

# Import the Robyn API from api.py
api_module = importlib.import_module("api")

# Start the API if it's not already running
if 'api_thread' not in st.session_state:
    api_thread = threading.Thread(target=start_api, daemon=True)
    api_thread.start()
    time.sleep(2)  # Allow some time for the server to start
# Base URL for the Robyn backend
BASE_URL = "http://localhost:8080"  # Adjust if necessary

# Title of the app
st.title("Task Manager")

# Section to create a new task
st.header("Create a New Task")
task_name = st.text_input("Task Name")
if st.button("Create Task"):
    response = requests.post(f"{BASE_URL}/task", json={"name": task_name})
    if response.status_code == 201:
        st.success("Task created successfully!")
    else:
        st.error("Error creating task.")

# Section to fetch and display tasks
st.header("Get Task by ID")
task_id = st.text_input("Enter Task ID")
if st.button("Fetch Task"):
    response = requests.get(f"{BASE_URL}/task/{task_id}")
    if response.status_code == 200:
        task = response.json()
        st.write(f"Task ID: {task['id']}, Name: {task['name']}, Status: {task['status']}")
    else:
        st.error("Task not found.")

