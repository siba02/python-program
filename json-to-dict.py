import json

json_string = {
  "id": 1,
  "name": "Alice",
  "age": 25
}
data = json.loads(json.dumps(json_string))
print(data)