import streamlit as st
import requests

# Set API URL
API_URL = "http://localhost:8080/task"

# Title of the app
st.title("Task Manager")

# Section to create a new task
st.header("Create a New Task")
task_name = st.text_input("Task Name")

if st.button("Create Task"):
    if task_name:
        # Send POST request to create a new task
        response = requests.post(API_URL, json={"name": task_name})
        if response.status_code == 201:
            st.success("Task created successfully!")
        else:
            st.error(f"Failed to create task: {response.text}")
    else:
        st.warning("Please enter a task name.")

# Section to display tasks
st.header("Tasks")
response = requests.get(API_URL)

# Check if the response was successful
if response.status_code == 200:
    try:
        # Attempt to parse the response as JSON
        tasks = response.json()
        for task in tasks:
            st.write(task['name'])
    except ValueError as e:
        # Handle JSON decoding errors
        st.error(f"Failed to decode JSON: {response.text}")
        st.error(f"Error details: {str(e)}")
else:
    # Log non-200 responses
    st.error(f"Failed to retrieve tasks. Status code: {response.status_code}")
    st.error(f"Response content: {response.text}")
