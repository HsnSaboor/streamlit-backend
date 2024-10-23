import streamlit as st
import requests
import subprocess
import os
import time

# Define the path to the API script
API_SCRIPT = 'api.py'

# Start the Robyn API server
def start_api():
    # Use subprocess to run the API server in a separate process
    process = subprocess.Popen(['python', API_SCRIPT], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(2)  # Allow some time for the server to start
    return process

# Start the API if it's not already running
if 'api_process' not in st.session_state:
    st.session_state.api_process = start_api()

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
