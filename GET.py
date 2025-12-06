import requests
import json

url="https://jsonplaceholder.typicode.com/posts"
# url="https://api.ipapi.com/api/161.185.160.93"
response = requests.get(url)
data = response.json()
print(json.dumps(data, indent=4))