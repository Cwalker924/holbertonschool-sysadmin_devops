#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], arg=""):
    header = {"User-Agent": "Walker"}

    if (arg is None):
        return hot_list

    if (len(hot_list) == 0):
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        req = requests.get(url, headers=header)
        if ((req.status_code is 404) or ("data" not in req.json())):
            return (None)
        else:
            req = req.json()
            for post in req["data"]["children"]:
                hot_list.append(post["data"]["title"])

        return recurse(subreddit, hot_list)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, arg)
        req = requests.get(url, headers=header)
        if ((req.status_code is 404) or ("data" not in req.json())):
            return (None)
        else:
            req = req.json()
            for post in req["data"]["children"]:
                hot_list.append(post["data"]["title"])

        arg = req["data"]["after"]
        return recurse(subreddit, hot_list, arg)
