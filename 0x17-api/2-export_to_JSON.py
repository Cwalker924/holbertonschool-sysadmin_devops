#!/usr/bin/python3
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
import sys


if __name__ == "__main__":
        url = "https://jsonplaceholder.typicode.com/users"
        empId = sys.argv[1]
        user = requests.get("{}/{}"
                            .format(url, empId)).json()
        todos = requests.get("{}/{}/todos"
                             .format(url, empId)).json()
        uid = user.get("id")
        uname = user.get("username")
        utask = []
        udict = {}

        for todo in todos:
                uinfo = {}
                uinfo["task"] = todo.get("title")
                uinfo["completed"] = todo.get("completed")
                uinfo["username"] = uname
                utask.append(uinfo)

        udict[str(uid)] = utask
        with open("{}.json".format(empId), mode="w", newline="") as tojson:
                json.dump(udict, tojson)
