import json

def create_json():
    # Create json file with information of your choice
    data = {
        "name": "Abdullah",
        "age": 26,
        "city": "Helsnki"
    }

    with open('data.json', 'w') as f:
        json.dump(data, f,indent=5, sort_keys=False)

def read_json():
    # Read json file
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

def delete_json():
    # Delete json file
    with open('data.json', 'w') as f:
        pass

