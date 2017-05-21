#!/usr/bin/python3
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    head = {"User-Agent": "Walker"}
    req = requests.get(url, headers=head)
    if (("data" not in req.json()) or (req.status_code is 404)):
        print("None")
    else:
        req = req.json()
        for post in req["data"]["children"]:
            print(post["data"]["title"])
