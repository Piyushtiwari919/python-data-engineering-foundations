import json

valid_llm_response = '{"movie":{"metadata":{"actors":[{"name":"Leonardo DiCaprio","role":"Cobb"},{"name":"Joseph Gordon-Levitt","role":"Arthur"}],"year":2010,"genre":"Science Fiction"}}}'

broken_llm_response = """```json
{"movie":{"metadata":{"actors":[{name":"Leonardo DiCaprio","role":"Cobb"},{"name":"Joseph Gordon-Levitt","role":"Arthur"}],"year":2010,"genre":"Science Fiction"}}}
```"""


def brittle_extract(json_string):
    data = json.loads(json_string)
    print(data["movie"]["metadata"]["actors"][0]["name"])


def safe_extraction(json_string):
    try:
        stripped_string = json_string.strip("```json").strip("```").strip()
        original_data = json.loads(stripped_string)
        actors = original_data.get("movie",{}).get("metadata",{}).get("actors",[])
        
        if not actors:
            return "No actor present"
        
        actor = actors[0]
        
        name = actor.get("name","Not Found")
        return name
    except json.JSONDecodeError as e:
        print(f"Failed to parse LLM JSON: {e}")
        return None


def main() -> None:
    brittle_extract(valid_llm_response)
    print(safe_extraction(valid_llm_response))
    print(safe_extraction(broken_llm_response))


if __name__ == "__main__":
    main()
