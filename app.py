# app.py
import streamlit as st
import requests

API_URL = "http://localhost:8000/task"

st.set_page_config(page_title="Task Manager", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Create Task", "View Tasks"])

# Create Task Page
if selection == "Create Task":
    st.title("Create a New Task")
    task_name = st.text_input("Task Name")

    if st.button("Create Task"):
        if task_name:
            response = requests.post(API_URL, json={"name": task_name})
            if response.status_code == 201:
                st.success("Task created successfully!")
            else:
                st.error(f"Failed to create task: {response.text}")
        else:
            st.warning("Please enter a task name.")

# View Tasks Page
elif selection == "View Tasks":
    st.title("View Tasks")
    response = requests.get(API_URL)

    if response.status_code == 200:
        tasks = response.json()
        if tasks:
            for task in tasks:
                st.write(task['name'])
        else:
            st.write("No tasks available.")
    else:
        st.error(f"Failed to retrieve tasks. Status code: {response.status_code}")
        st.error(f"Response content: {response.text}")
