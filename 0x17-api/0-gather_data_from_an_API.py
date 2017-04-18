#!/usr/bin/pyhton3
"""
a Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import json
import sys


def user_info(uid):
    """
    Gets user info from API
    Arguement: in user id
    """
    url = "https://jsonplaceholder.typicode.com"
    empId = sys.argv[1]
    comp = []

    name = requests.get("{}/users/{}"
                        .format(url, empId)).json().get("name")
    todo = requests.get("{}/todos?userId={}".format(url, empId)).json()

    for jobs in todo:
        if jobs.get("completed") is True:
            comp.append(jobs.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(comp), len(todo)))
    for task in comp:
        print("\t{}".format(task))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            uid = sys.argv[1]
            user_info(uid)
        except (ValueError, TypeError):
            pass
