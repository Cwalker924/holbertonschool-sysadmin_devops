#!/usr/bin/pyhton3
"""
a Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.

Formart must be:

{ "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}}, {"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}

Then save to json file
"""
import json
import requests


if __name__ == "__main__":
        usersurl = "https://jsonplaceholder.typicode.com/users"
        todourl = "https://jsonplaceholder.typicode.com/todos"
        users = requests.get(usersurl).json()
        todos = requests.get(todourl).json()
        utask = []
        udict = {}

        for user in users:
                uid = user.get("id")
                uname = user.get("username")
                udict[str(uid)] = utask

                for todo in todos:
                        uinfo = {}
                        uinfo["task"] = todo.get("title")
                        uinfo["completed"] = todo.get("completed")
                        uinfo["username"] = uname
                        utask.append(uinfo)
                udict[str(uid)] = utask

        with open("todo_all_employees.json", mode="w", newline="") as tojson:
                json.dump(udict, tojson)
