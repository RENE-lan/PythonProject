import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"].strip()
    if todo:
        todos.append(todo + "\n")
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("Increase your productivity")


for index, todo in enumerate(todos):
    if st.checkbox(todo.strip(), key=todo):
        todos.pop(index)
        functions.write_todos(todos)
        st.experimental_rerun()
        break


st.text_input("Add new todo:", key="new_todo", on_change=add_todo)
