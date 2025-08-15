import requests

url = "http://127.0.0.1:5000/video/1"
payload = {"likes": 10, "title": "My Video"}

res = requests.put(url, json=payload)
print(res.json())


import requests

url = "http://127.0.0.1:5000/video/2"
payload = {"likes": 25, "title": "Form Video"}

res = requests.put(url, data=payload)
print(res.json())
