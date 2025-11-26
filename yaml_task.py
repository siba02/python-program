import yaml
with open("docker-compose-basic-nrf.yaml") as f:
    data = yaml.safe_load(f)
# print(data["services"]["mysql"]["environment"]["MYSQL_USER"])

# conver to dictionary then retrive
# env_list = data["services"]["oai-amf"]["environment"]

# env_dict = {}

# for item in env_list:
#     key, value = item.split("=")
#     env_dict[key] = value

# print(env_dict["MCC"])


# using for loop retrive all environment variables and then split
for env in data["services"]["oai-amf"]["environment"]:
    if "MCC" in env:
        print(env.split("=")[1])
