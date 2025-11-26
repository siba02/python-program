import json
import yaml

with open("wiresh.json") as f:
    data = json.load(f)

yaml_data = yaml.dump(data, sort_keys=False, indent=4)
print(yaml_data)