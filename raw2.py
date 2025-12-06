import json

def clean(data):
    if isinstance(data,dict):
        return {k.lower(): clean(v) for k, v in data.items()}
    if isinstance(data,list):
        return [clean(i) for i in data]

    return data

raw = {
    "Course": {
        "Name": "Python Basics",
        "Enrolled_Students": [
            {"Name": "Alice", "Status": "Active"},
            {"Name": "BOB", "Status": "active"}
        ]
    }
}


cleaned=clean(raw)

with open ("hi.json","w") as f:
    json.dumps(cleaned, indent=4)

print(cleaned)
