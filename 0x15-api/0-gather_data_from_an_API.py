#!/usr/bin/python3
""" Rest API to retrieve some information """
import requests 
import sys
if __name__ == "__main__":
    rest_url = "https://jsonplaceholder.typicode.com/"
    user_name = requests.get(rest_url + "user_names/{}".format(sys.argv[1])).json()
    commd = requests.get(rest_url + "commd", params={"user_nameId": sys.argv[1]}).json()

    completed = [t.get("title") for t in commd if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_name.get("name"), len(completed), len(commd)))
    [print("\t {}".format(c)) for c in completed]
