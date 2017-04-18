#!/usr/bin/pyhton3
import requests
import json
import csv
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    empId = sys.argv[1]
    lstform = []
    if len(sys.argv) < 2:
        print("Need Employee ID")
    else:
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
