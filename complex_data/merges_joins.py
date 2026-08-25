import pandas as pd

# MongoDB Profile
df_users = pd.DataFrame(
    {
        "user_id": [1, 2, 3, 4, 5, 6],
        "username": ["akash", "amit", "vikash", "golu", "pawan", "kisan"],
        "signup_tier": ["Free", "Premium", "Free", "Free", "Premium", "Free"],
    }
)

df_payments = pd.DataFrame(
    {
        "transaction_id": [989, 891, 652, 894, 519],
        "user_id": [1, 2, 3, 4, 99],
        "amount_paid": [1200, 1000, 2100, 100, 500],
    }
)


def main() -> None:
    # Inner Join
    inner_join_df = pd.merge(df_users, df_payments, on="user_id")
    print(inner_join_df)

    # Left Join
    left_join_df = pd.merge(df_users, df_payments, how="left", on="user_id")
    print(left_join_df)
    
    #outer join with ghost transaction
    outer_join_df = pd.merge(df_users, df_payments, how="outer", on="user_id")
    ghost_transaction = outer_join_df[outer_join_df["username"].isna() | outer_join_df["signup_tier"].isna()]
    print(ghost_transaction)


if __name__ == "__main__":
    main()
