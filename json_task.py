import json
with open("wiresh.json") as f:
    data = json.load(f)
# print(data[0]["_source"]["layers"]["eth"]["eth.dst"])
print(data[0]["_index"])
