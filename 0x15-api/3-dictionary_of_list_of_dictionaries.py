#!/usr/bin/python3
"""A Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress
and exports data in JSON format."""
import json
import requests
import sys


def export_to_json(all_todos):
    json_file_name = "todo_all_employees.json"
    with open(json_file_name, mode='w') as json_file:
        json.dump(all_todos, json_file)

    print("JSON Data exported to: {}".format(json_file_name))


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    all_todos = {}

    for employee_id in range(1, 11):
        # Make a request to get user information
        user_response = requests.get(url + "users/{}".format(employee_id))
        # Check if the user exists
        if user_response.status_code != 200:
            print("Error: User not found.")
            continue

        # Extract user information
        user = user_response.json()
        # Make a request to get TODO items for the user
        todos_response = requests.get(url + "todos",
                                      params={"userId": employee_id})
        todos = todos_response.json()
        # Build JSON data for all employees
        all_todos[user["id"]] = [{"username": user["username"],
                                  "task": todo["title"],
                                  "completed": todo["completed"]}
                                 for todo in todos]

    # Export data to JSON file
    export_to_json(all_todos)
