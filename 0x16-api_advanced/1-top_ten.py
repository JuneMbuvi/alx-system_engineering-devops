#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """prints the titles of the
    first 10 hot posts listed for a given subreddit"""
    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "RedditPostFetcher/1.0"}

    response = requests.get(endpoint, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            title = post.get("data", {}).get("title", "")
            print(title)
    elif response.status_code == 404:
        print("None")
    else:
        print("None")
