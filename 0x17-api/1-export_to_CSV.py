#!/usr/bin/pyhton3
"""
a Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    empId = sys.argv[1]
    lstform = []
    uname = requests.get("{}/users/{}"
                         .format(url, empId)).json().get("username")
    todo = requests.get("{}/todos?userId={}".format(url, empId)).json()

    with open("{}.csv".format(empId), mode="w", newline="") as thecsv:
        writecsv = csv.writer(thecsv, delimiter=",", quotechar='"',
                              quoting=csv.QUOTE_ALL)
        for info in todo:
            uid = info.get("id")
            status = info.get("completed")
            title = info.get("title")
            row = [empId, uname, status, title]
            writecsv.writerows([row])
