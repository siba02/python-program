import json

def clean(data):
    if isinstance(data, dict):
        return {k.lower(): clean(v) for k, v in data.items()}
    if isinstance(data, list):
        return [clean(i) for i in data]
    return data

raw = {"config": {"Site": "Bangalore", "Devices": 12}}

cleaned = clean(raw)

print(cleaned)
