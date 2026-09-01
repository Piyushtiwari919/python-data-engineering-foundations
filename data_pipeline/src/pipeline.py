from src import cleaner
from src import validator
import pandas as pd


def run_pipeline():
    user_df1 = cleaner.clean_user_csv()
    user_list = validator.load_and_validate_jsons(
        "data/raw/api_responses", "schema/user_schema.json"
    )
    user_df2 = pd.DataFrame(user_list)
    final_df = pd.merge(
        user_df2, user_df1, left_on="user_id", right_index=True, how="inner"
    )
    final_df.to_parquet("data/processed/merged_users.parquet", index=False)
