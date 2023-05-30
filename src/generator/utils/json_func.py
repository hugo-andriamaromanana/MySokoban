import json

def get_json(path: str):
    with open(path, 'r') as f:
        data=json.loads(f.read())
    return data

def json_dump(file_path: str, data: dict):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
        