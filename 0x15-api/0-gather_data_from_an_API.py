#!/usr/bin/python3
"""A Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # Check if the script is provided with an ID is a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Parse the employee ID from the command-line argument
    employee_id = sys.argv[1]

    # Make a request to get user information
    user_response = requests.get(url + "users/{}".format(employee_id))

    # Check if the user exists
    if user_response.status_code != 200:
        print("Error: User not found.")
        sys.exit(1)

    # Extract user information
    user = user_response.json()

    # Make a request to get TODO items for the user
    todos_response = requests.get(url + "todos",
                                  params={"userId": employee_id})
    todos = todos_response.json()

    # Filter completed TODO items
    finished = [todo["title"] for todo in todos if todo.get("completed")]

    # Print the results
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          len(finished),
                                                          len(todos)))
    for finish in finished:
        print("\t{}".format(finish))
