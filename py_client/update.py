import requests

endpoint = "http://localhost:8000/api/products/5/update/"


data = {
    "title" : "Hello there my old friend",
    "price" : 16969.98
}

get_response = requests.put(endpoint, json=data)

'''
print(get_response.headers)

In it's result, we can check the value of field 'Content-Type' and see for
ourselves that the returned value is of type json.
'''
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
# This will raise an error if get request made above is returning data
# by HttpResponse as it returns a text/html type string.
# This can clearly be seen by printing the header.