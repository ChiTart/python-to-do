# TO-DO LIST MANAGER
## Video Demo: 
https://youtu.be/IgrGlrHn5p4

## Description:

This To-Do List Manager was made as a CS50P final project.
It is a Python-based console application designed to help users manage their tasks with ease.
The application offers features that allow users to add new tasks, mark tasks as completed, and display the entire list. Incomplete tasks appear first, while completed ones are listed at the end.

### Project structure

project.py

test_project.py

requirements.txt

README.md

### Libraries
__json__: A Python library for encoding and decoding JSON data, facilitating easy interchange of data between different programming languages. Find more [here](https://docs.python.org/3/library/json.html)

__pytest__: A Python testing framework that simplifies and enhances the testing process, offering concise syntax, detailed reporting, and robust fixture support. Find more [here](https://docs.pytest.org/en/7.1.x/contents.html)

### Main features

At the opening, the application will call the load_todo_list() function.
This will load the users' lists from their previous session or, if it's their first session, it will create three new empty lists.

By pressing "1," users will call the add_item() function and add new tasks to their lists.

By pressing "2," they can mark tasks as completed using the mark_complete() function.

By pressing "3," they can display the entire list through the display_todo_list() function.
Note that incomplete tasks appear first, while the completed ones are at the end of the list. This will help the users focusing on the job-to-be-done.

Additionally, users can clear the list of completed tasks by pressing "4" and calling the clear_todo_list() function.

The To-Do List Manager also provides users with the ability to switch between three different lists: personal, work, and shopping. This feature allows them to keep their personal tasks separate from work-related activities and shopping lists. The application constantly reminds users which list is currently open to ensure ease of use.
With command 5, users can call the switch_todo_list() function and switch between these lists.

To save the three lists and exit the program, the user must just insert the command "6".
The application will call the save_todo_list() first and then quit.
This will create a JSON file storing the users' lists, enabling them to find their tasks and related statuses in the next session.
If the file already exists, the application will just update it.

### Error handling
To ensure the smooth functioning of the application, the main errors that could happen are handled effectively.
If the user enters an invalid command, the application does not crash and instead prompts the user to enter a valid command.

Similarly, if a user marks a task as completed that is not present in the current to-do list, the application informs the user that the item was not found in the current list.
This will enable users to use the application without any frustration and make their experience seamless.
