import streamlit as st

# Navigation
if st.sidebar.button("Tasks"):
    st.experimental_set_query_params(page="tasks")
elif st.sidebar.button("Data"):
    st.experimental_set_query_params(page="data")

# Handle routing
page = st.experimental_get_query_params().get("page", ["tasks"])[0]
if page == "tasks":
    st.title("Tasks Page")
    # Render tasks here
elif page == "data":
    st.title("Data Page")
    # Render data here
