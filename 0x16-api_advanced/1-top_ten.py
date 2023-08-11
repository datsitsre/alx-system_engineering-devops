#!/usr/bin/python3
'''
Print the ten titles
'''

import requests
import json


def top_ten(subreddit):
    """
    Return the top titles of a given subreddit
    """
    url_link = "https://www.reddit.com/r/{}/hot.json?limit=10"

    get_info = requests.get(url_link.format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirections=False)

    if get_info.status_code >= 300:
        print("None")
        return

    data_out = response.json().get("data")
    [print(c.get("data").get("title"))
     for c in results.get("children")]
