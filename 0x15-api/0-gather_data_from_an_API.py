#!/usr/bin/python3
"""
This script retrieves and displays the progress of a specific employee's
to-do list from the JSONPlaceholder API.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Arguments:
    <employee_id> - An integer representing the employee ID.

The script outputs:
    - Employee's name
    - Number of completed tasks and total number of tasks
    - Titles of completed tasks, each prefixed by a tab and a space.
"""

import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetches employee data and their to-do list from the JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the user data and a list of to-dos.
    """
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(employee_id))
    todos_response = requests.get(url + "todos", params={"userId": employee_id})

    # Check if the API responses are successful
    if user_response.status_code != 200 or todos_response.status_code != 200:
        raise Exception("Error: Unable to fetch data")

    user = user_response.json()
    todos = todos_response.json()

    return user, todos


def print_employee_todo_progress(user, todos):
    """
    Prints the progress of the employee's to-do list.

    Args:
        user (dict): The user data.
        todos (list): The list of to-dos.
    """
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    total_tasks = len(todos)
    done_tasks = len(completed)
    
    # Print the formatted output
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), done_tasks, total_tasks))
    
    for task in completed:
        print("\t {}".format(task))


def main():
    """
    Main function to handle command line arguments and process data.
    """
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        return

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        return

    try:
        user, todos = fetch_employee_data(emp_id)
        print_employee_todo_progress(user, todos)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
