#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
   if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        return
    
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        return
    
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(emp_id))
    todos_response = requests.get(url + "todos", params={"userId": emp_id})
    
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data")
        return
    
    user = user_response.json()
    todos = todos_response.json()
    
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    total_tasks = len(todos)
    done_tasks = len(completed)
    
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), done_tasks, total_tasks))
    
    for task in completed:
        print("\t {}".format(task))
