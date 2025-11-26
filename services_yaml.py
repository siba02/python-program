import yaml

with open("docker-compose-basic-nrf.yaml") as f:
    data = yaml.safe_load(f)

for name, service in data["services"].items():
    ip = list(service.get("networks", {}).values())[0].get("ipv4_address")
    deps = service.get("depends_on", [])
    print(f"{name} -> IP: {ip}, Depends On: {deps}")