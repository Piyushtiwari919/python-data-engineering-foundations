from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "person": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "number", "minimum": 19},
                "address": {
                    "type": "object",
                    "properties": {
                        "street": {"type": "string"},
                        "city": {"type": "string"},
                    },
                },
            },
            "required": ["name"],
        }
    },
    "required": ["person"],
}

data = {
    "person": {
        "name": "Akash",
        "age": 19,
        "address": {
            "street": "123 Main St",
            "city": "Springfield",
        },
    }
}


def main() -> None:
    try:
        validate(instance=data, schema=schema)
        print("JSON data is valid")
    except ValidationError as e:
        print(f"JSON data is invalid: {e.message}")


if __name__ == "__main__":
    main()
