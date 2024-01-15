import pytest
from project import add_item, mark_complete, display_todo_list, clear_todo_list

def test_add_item():
    todo = {}
    add_item(todo, "Buy groceries")
    assert len(todo) == 1
    assert "Buy groceries" in todo.keys()
    assert todo["Buy groceries"] == False


def test_mark_complete():
    todo = {"Buy groceries": False}
    mark_complete(todo, "Buy groceries")
    assert todo["Buy groceries"] == True


def test_display_todo_list(capsys):
    todo = {"Buy groceries": False, "Do laundry": True}
    display_todo_list(todo)
    captured = capsys.readouterr()
    assert "To-Do List:" in captured.out
    assert "- Buy groceries (TO DO)" in captured.out
    assert "- Do laundry (Done)" in captured.out


def test_clear_todo_list():
    todo = {"Buy groceries": False, "Do laundry": True}
    clear_todo_list(todo)
    assert todo == {"Buy groceries": False}
