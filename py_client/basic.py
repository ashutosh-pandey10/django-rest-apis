import requests

endpoint = "http://localhost:8000/api"

get_response = requests.get(endpoint, json={"query":"Hello World"})

print(get_response.headers)
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
# This will raise an error if get request made above is returning data
# by HttpResponse as it returns a text/html type string.
# This can clearly be seen by printing the header.