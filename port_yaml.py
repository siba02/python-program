import yaml

with open("docker-compose-basic-nrf.yaml") as f:
    data = yaml.safe_load(f)

seen_ports = set()

for name, service in data["services"].items():
    for env in service.get("environment", []):
        if "PORT" in env.upper():  # consider only envs with PORT
            port_name, port_value = env.split("=")
            if port_value not in seen_ports:
                print(f"{name}: {port_name} = {port_value}")
                seen_ports.add(port_value)