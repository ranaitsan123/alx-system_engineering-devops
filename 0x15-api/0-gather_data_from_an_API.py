#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee whose TODO list is to be fetched.

    Returns:
        None
    """
    # Define the API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to get user data for employee ID {employee_id}")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name', 'Unknown')

    # Fetch TODO list data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to get TODO list data for employee ID {employee_id}")
        return

    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = [todo['title'] for todo in todos_data if todo['completed']]
    number_of_done_tasks = len(completed_tasks)

    # Print the result
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"     {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("EMPLOYEE_ID must be an integer.")
        sys.exit(1)

