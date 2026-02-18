#!/usr/bin/python3
""" return top ten"""

import requests


def top_ten(subreddit):
   url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0-top-ten:v1.0 (by /u/Natnael)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts[:10]:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
