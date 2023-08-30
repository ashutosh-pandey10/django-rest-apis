import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?\n")
password = getpass("What's your passcode?\n")

get_auth = requests.post(auth_endpoint, data={"username" : username, "password" : password})

if get_auth.status_code == 200:
    token = get_auth.json()["token"]
    auth_header = {
        "Authorization" : f"Bearer {token}"
    }
    print(token)

    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=auth_header)

    print(get_response.json())