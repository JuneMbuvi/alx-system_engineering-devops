#!/usr/bin/python3
"""function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns number of subs"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "RedditSubscribers/1.0"}
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    elif response.status_code == 404:
        return 0
    else:
        return 0
