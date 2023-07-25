#!/usr/bin/python3
""" Rest API to retrieve some information """
import requests
import sys
if __name__ == "__main__":
    rest_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(rest_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(rest_url + "todos", params={"userId": sys.argv[1]}).json()

    cmmd = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(cmmd), len(todos)))
    [print("\t {}".format(c)) for c in cmmd]
