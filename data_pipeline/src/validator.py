import json
import jsonschema
from pathlib import Path




def load_and_validate_jsons(directory_path, schema_path):
    directory_path = Path(directory_path)
    schema = {}
    with open(schema_path) as f:
        schema = json.load(f)

    list_users = []
    for file_path in directory_path.glob("*.json"):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                json_data = json.load(f)
                try:
                    jsonschema.validate(instance=json_data, schema=schema)
                    list_users.append(json_data)
                except jsonschema.ValidationError as e:
                    print(f"Error occured in validating json : {e}")
                # print(f"Successfully loaded: {file_path.name}")
            except json.JSONDecodeError as e:
                print(
                    f"Error: {file_path.name} is not a valid JSON file. Error:{e.msg}"
                )
    return list_users
