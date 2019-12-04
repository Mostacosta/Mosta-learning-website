import requests
import json

url = "http://127.0.0.1:8000/api/user"

new_data = {
    "username": "mokomsdmjklfnjjk",
    "email": "mostafaelhassan910@gmail.com",
    "password":"mosta23456",
    "password2":"mosta23456",
    "degree": "0",
}
data = {
    "user": {
        "username": "skmetsh",
        "email": "mostafaelhassan910@gmail.com",
        "password":"mosta23456",
        "password2":"mosta23456",
    },
    "degree": "0",
}
r = requests.post(url,data=new_data)
print(r.text)
print(r.json)