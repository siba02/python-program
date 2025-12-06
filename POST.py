import requests
import json

url="https://jsonplaceholder.typicode.com/posts"
data={'title': 'foo',
       'body': 'bar',
         'userId': 1
         }
response = requests.post(url,data )
print(json.dumps(response.json(), indent=4))
