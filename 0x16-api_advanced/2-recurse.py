#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles
    of all hot articles for a given subreddit"""
    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "RedditPostFetcher/1.0"}
    if after:
        endpoint += f"&after={after}"

    response = requests.get(endpoint, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        hot_list.extend([post.get("data", {}).get("title", "")
                         for post in posts])
        after = data.get("data", {}).get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 404:
        return None
    else:
        return None
