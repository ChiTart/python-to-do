import json

def main():

    """
    Main function to manage the to-do list manager program.
    """

    current_list = "Personal"
    todo_lists = load_todo_list()

    while True:

        print("\n––––––––––––––––––––––––––––––––––––––––––")
        print(f"Welcome to your to-do list manager!")
        print(f"You are currently using your '{current_list}' list\n")
        print("Enter...")
        print("1 to add a new item 📝")
        print("2 to mark an item as completed ✅")
        print("3 to display the current list 🗒️")
        print("4 to clear completed tasks from the list 🧹")
        print("5 to switch to a different to-do list 🔄")
        print("6 to quit ❌")
        print("––––––––––––––––––––––––––––––––––––––––––\n")


        command = input("Enter the next command: ")
        match command:
            case "1":
                item = input("Enter the task: ")
                add_item(todo_lists[current_list], item, current_list)
            case "2":
                item = input("Enter the task to mark as complete: ")
                mark_complete(todo_lists[current_list], item, current_list)
            case "3":
                display_todo_list(todo_lists[current_list], current_list)
            case "4":
                clear_todo_list(todo_lists[current_list])
            case "5":
                current_list = switch_todo_list(current_list, list(todo_lists.keys()))
            case "6":
                save_todo_list(todo_lists)
                break
            case _:
                print("Invalid command\nPlease enter a number between 1 and 5")
                continue


def add_item(todo_list, item, current_list):

    """
    Add a new item to the specified to-do list.

    :param todo_list: The to-do list to which the item will be added.
    :type todo_list: dict
    :param item: The task to add.
    :type item: str
    :param current_list: The name of the current to-do list.
    :type current_list: str

    :return: None
    """

    todo_list.update({item: False})
    print(f"'{item}' added to the {current_list} list.")


def mark_complete(todo_list, item, current_list):

    """
    Mark a task as complete in the current to-do list.

    :param todo_list: The to-do list containing the task.
    :type todo_list: dict
    :param item: The task to mark as complete.
    :type item: str

    :return: None
    """

    for task in todo_list.keys():
        if task == item:
            todo_list[task] = True
            print(f"'{item}' marked as complete.")
            return
    print(f"'{item}' not found in the {current_list} list.")


def display_todo_list(todo_list, current_list):

    """
    Display the to-do list sorted by completion status.

    :param todo_list: The to-do list to display.
    :type todo_list: dict
    :param current_list: The name of the current to-do list.
    :type current_list: str
    :param current_list: The name of the current to-do list.
    :type current_list: str

    :return: None
    """

    sorted_dict = dict(sorted(todo_list.items(), key=lambda x:x[1]))
    print("\n––––––––––––––––––––––––––––––––––––––––––")
    print(f"{current_list} To-Do List:")
    for task, status in sorted_dict.items():
        status_str = "Done" if status else "TO DO"
        print(f"- ({status_str}) {task}")
    print("––––––––––––––––––––––––––––––––––––––––––\n")


def switch_todo_list(current_list, lists):

    """
    Switch to a different to-do list.

    :param current_list: The name of the current to-do list.
    :type current_list: str
    :param lists: The available to-do lists.
    :type lists: list

    :return: The name of the selected to-do list.
    :rtype: str
    """

    print("Available To-Do Lists:")
    for index, list_name in enumerate(lists, start=1):
        print(f"{index}. {list_name}")

    try:
        choice = int(input("Enter the number of the list you want to switch to: "))
        if 1 <= choice <= len(lists):
            selected_list = lists[choice - 1]
            print(f"Switched to the '{selected_list}' to-do list.")
            return selected_list
        print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return current_list


def save_todo_list(todo_list, filename="todo_list.json"):

    """
    Save the to-do list to a JSON file.

    :param todo_list: The to-do list to save.
    :type todo_list: dict
    :param filename: The name of the file to save to. Default is "todo_list.json".
    :type filename: str

    :return: None
    """

    with open(filename, "w") as file:
        json.dump(todo_list, file)


def load_todo_list(filename="todo_list.json"):

    """
    Load the to-do list from a JSON file.

    :param filename: The name of the file to load from. Default is "todo_list.json".
    :type filename: str

    :return: The loaded to-do list.
    :rtype: dict
    """

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"Personal": {}, "Work": {}, "Shopping": {}}


def clear_todo_list(todo_list):

    """
    Clear completed tasks from the to-do list.

    :param todo_list: The to-do list to clear completed tasks from.
    :type todo_list: dict

    :return: None
    """

    incomplete_tasks = {task: status for task, status in todo_list.items() if not status}
    todo_list.clear()
    todo_list.update(incomplete_tasks)


if __name__ == "__main__":
    main()
