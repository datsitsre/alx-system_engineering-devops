#!/usr/bin/python3
""" Rest to store json file """
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    rest_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(rest_url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(rest_url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
