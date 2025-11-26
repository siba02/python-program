# fetch the route information and convert it to JSON format
# import route_info
import json     
route_data = get_route_data()
json_data = json.dumps(route_data, indent=4)
print(json_data)    
