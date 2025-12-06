items = []

def add_item(payload=None):
    if not payload or not isinstance(payload, dict):
        return "Error: No payload provided"
    items.append(payload)
    return "Item added successfully"

def get_items():
    if not items:
        return "No items available"
    return {"items": items}

def handle(request, payload=None):
    try:
        # Split method and path safely
        method, path = request.split(maxsplit=1)

        # GET /items → return all items
        if method == "GET" and path == "/items":
            return get_items()

        # POST /items → add a new item
        elif method == "POST" and path == "/items":
            return add_item(payload)

        # invalid route
        else:
            return "Error: Invalid method or path"

    except Exception as e:
        return f"Error: {str(e)}"


# Test calls
print(handle("POST /items", {"title": "Book A", "status": "available"}))
print(handle("GET /items"))
