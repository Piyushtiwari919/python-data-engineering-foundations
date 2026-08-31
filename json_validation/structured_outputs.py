from pydantic import BaseModel, Field,ValidationError
import json
from typing import Annotated


class ProductReview(BaseModel):
    product_name: str
    sentiment_score: Annotated[int, Field(ge=1, le=10)]
    key_features: list[str]


llm_valid_mock_output = {
    "product_name": "mac",
    "sentiment_score": 8,
    "key_features": ["Fast Charging", "Long Battery Life", "High Speed"],
}

llm_invalid_mock_output = {
    "product_name": "mac",
    "sentiment_score": "eight",
    "key_features": ["Fast Charging", "Long Battery Life", "High Speed"],
}


def main() -> None:
    try:
        product1 = ProductReview.model_validate_json(json.dumps(llm_invalid_mock_output))
    except ValidationError as e:
        print(f"JSON data is invalid: {e.errors()}")

if __name__ == "__main__":
    main()
