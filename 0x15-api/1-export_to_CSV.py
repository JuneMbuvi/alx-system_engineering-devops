#!/usr/bin/python3
"""A Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress and exports data in CSV format"""
import csv
import requests
import sys


def using_csv(user_id, user, todos):
    """a function to export employee data using csv"""
    filename = f"{user_id}.csv"

    with open(filename, mode="w", newline='') as f:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(f, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        writer.writeheader()
        for todo in todos:
            task_stat = "True" if todo.get("completed") else "False"
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": user.get("username"),
                "TASK_COMPLETED_STATUS": task_stat,
                "TASK_TITLE": todo.get("title")
            })


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()

    # Make a request to get TODO items for the user
    todos_response = requests.get(url + "todos",
                                  params={"userId": employee_id})
    todos = todos_response.json()
    finished = [todo["title"] for todo in todos if todo.get("completed")]

    """print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          len(finished),
                                                          len(todos)))"""
    using_csv(employee_id, user, todos)
