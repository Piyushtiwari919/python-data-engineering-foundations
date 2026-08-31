import json

complex_llm_string = """
{
  "request_id": "req_9982",
  "data": {
    "candidates": [
      {
        "name": "Piyush",
        "skills": {
          "primary": "Python",
          "secondary": "Node.js"
        }
      }
    ]
  }
}
"""


def parse_llm_output(raw_string):
    try:
        # 1. Clean the string (LLMs love wrapping JSON in markdown)
        clean_string = raw_string.strip("```json").strip("```").strip()

        # 2. Parse safely
        data = json.loads(clean_string)

        # 3. Extract defensively using .get()
        # If "data", "candidates", or the first candidate is missing, handle it safely.
        candidates = data.get("data", {}).get("candidates", [])

        if not candidates:
            return "No candidates found."

        first_candidate = candidates[0]
        # Chain .get() safely
        primary_skill = first_candidate.get("skills", {}).get(
            "primary", "Unknown Skill"
        )
        return primary_skill

    except json.JSONDecodeError as e:
        print(f"Failed to parse LLM JSON: {e}")
        return None


def main() -> None:
    print(parse_llm_output(complex_llm_string))


if __name__ == "__main__":
    main()
