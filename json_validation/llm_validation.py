from pydantic import BaseModel
from openai import OpenAI

#Mock Implementation
client = OpenAI()

# 1. Define the Schema using Pydantic (This replaces manual jsonschema)
class UserExtraction(BaseModel):
    name: str
    age: int
    is_active: bool

# 2. Pass the Pydantic class directly to the LLM's 'response_format'
completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Extract info for Piyush, he is 20 and active."}
    ],
    response_format=UserExtraction, # <-- THIS IS THE GUARDRAIL
)

# 3. The output is perfectly parsed and typed. No json.loads() required!
user_data = completion.choices[0].message.parsed
print(user_data.name) # "Piyush"
print(type(user_data.age)) # <class 'int'>