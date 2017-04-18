#!/usr/bin/pyhton3
import requests
import json
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    empId = sys.argv[1]
    comp = []
    if len(sys.argv) < 2:
        print("Need Employee ID")
    else:
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
