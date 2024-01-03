import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from todo_list import ToDoList


def test_add_task():
    todo_list = ToDoList()
    todo_list.add_task("Buy groceries")
    assert "Buy groceries" in todo_list.list_tasks()

def test_list_tasks():
    todo_list = ToDoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Pay bills")
    assert todo_list.list_tasks() == ["Buy groceries", "Pay bills"]

def test_mark_as_completed():
    todo_list = ToDoList()
    todo_list.add_task("Buy groceries")
    todo_list.mark_as_completed("Buy groceries")
    assert todo_list.tasks[0]["status"] == "Completed"

def test_clear_tasks():
    todo_list = ToDoList()
    todo_list.add_task("Buy groceries")
    todo_list.clear_tasks()
    assert not todo_list.tasks
