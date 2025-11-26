import yaml
import json


with open("docker-compose-basic-nrf.yaml") as f:
    data = yaml.safe_load(f)

jason_data = json.dumps(data, indent=4) 
print(jason_data)

