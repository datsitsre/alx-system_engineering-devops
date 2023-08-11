#!/usr/bin/python3
'''
Query the Reddit Api
'''
import json
import requests


def number_of_subscribers(subreddit):
    '''
    Query for the subcribers
    '''
    url_link = "https://www.reddit.com/r/{}/about.json"

    get_subcribers = requests.get(url_link.format(subreddit),
                                  headers={"User-Agent": "My-User-Agent"},
                                  allow_redirects=False)

    if get_subcribers.status_code >= 300:
        return 0

    return get_subcribers.json().get("data").get("subscribers")
