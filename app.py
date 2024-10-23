import streamlit as st
import requests

# Define your API URL (make sure this matches where your API will be hosted)
API_URL = "http://localhost:8080"  # Change to your deployed API URL

def call_api(endpoint, method='GET', data=None):
    if method == 'POST':
        response = requests.post(f"{API_URL}/{endpoint}", json=data)
    else:
        response = requests.get(f"{API_URL}/{endpoint}")
    
    return response.json()

# Streamlit UI
st.title("My Streamlit App")

# Call API to get data
if st.button("Get Data"):
    result = call_api("data")
    st.write(result)

# Handle other interactions
