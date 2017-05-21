#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    Query's API and returns number of "subscribers" upon success, otherwise 0
    """
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {"User-Agent": "Walker"}
    req = requests.get(url, headers=head).json()
    if ("subscribers" in req["data"]):
        return(req["data"]["subscribers"])
    return (0)
