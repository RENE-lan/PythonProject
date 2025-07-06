import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip()
    if todo:
        todos.append(todo + "\n")  # Add newline for saving
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")



st.text_input(label="Add new todo:", placeholder="Enter a todo...", on_change=add_todo, key="new_todo")

