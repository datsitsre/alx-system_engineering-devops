#!/usr/bin/python3
"""
Recurse it
"""

import json
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    recursice function to quary reddit Api
    """
    url_link = "https://www.reddit.com/r/{}/hot.json"
    get_infor = requests.get(url_link.format(subreddit),
                             params={"count": count, "after": after},
                             headers={"User-Agent": "My-User-Agent"},
                             allow_redirects=False)

    if get_infor.status_code >= 400:
        return None

    list_title = hot_list + [sub.get("data")
                             .get("title")
                             for sub in get_infor.json()
                             .get("data")
                             .get("children")]

    list_info = get_infor.json()
    if not list_info.get("data").get("after"):
        return list_title

    return recurse(subreddit, list_title, list_info.get("data")
                   .get("count"), list_info.get("data")
                   .get("after"))
