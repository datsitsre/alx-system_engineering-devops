#!/usr/bin/python3
""" Rest APi to convert to CSV """
import csv
import os 
import sys
import requests


if __name__ == "__main__":
    user_name_id = sys.argv[1]
    rest_url = "https://jsonplaceholder.typicode.com/"
    user_info = requests.get(rest_url + "users/{}".format(user_name_id)).json()
    username = user_info.get("username")
    todos = requests.get(rest_url + "todos", params={"userId": user_name_id}).json()

    with open("{}.csv".format(user_name_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_name_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
