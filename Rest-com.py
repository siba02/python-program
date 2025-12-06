items=[]

def add_items(payload=None):
    if not payload:
        return "no data"
    items.append(payload)
    return "data added"

def get_items():
    if not items:
        return "item not available"
    return {"items":items}

def handle (request , payload=None):
    try:

        method ,path =request.split(maxsplit=1)

        if method =="GET" and path == "/items":
            return get_items()
        
        elif method == "POST" and path == "/items":
            return add_items(payload)
        
        else:
            return "invalid path"
        
    except Exception as e:
        return f"error:{str(e)}"

print(handle("POST /items",{"title":"A","status": "available"})) 
print(handle("GET /items"))

