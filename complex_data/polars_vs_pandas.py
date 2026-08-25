import csv
import random
import pandas as pd
import time
from functools import wraps
import polars as pl


# OUTPUT_FILE = "users.csv"
# NUM_ROWS = 5_000_000

# CITIES = ["New York", "London", "Tokyo", "Paris", "Sydney"]


# def generate_csv():
#     with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
#         writer = csv.writer(f)

#         # Header
#         writer.writerow(["user_id", "city", "age", "salary", "is_active"])

#         for user_id in range(1, NUM_ROWS + 1):
#             city = random.choice(CITIES)
#             age = random.randint(18, 80)
#             salary = round(random.uniform(30_000, 150_000), 2)
#             is_active = random.choice([True, False])

#             writer.writerow([user_id, city, age, salary, is_active])

#     print(f"Generated {NUM_ROWS:,} rows in {OUTPUT_FILE}")


def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Execution of {func.__name__} took run time of {run_time:.2f} seconds")
        return value

    return wrapper


@benchmark
def pandas_query() -> None:
    df = pd.read_csv("users.csv")

    filtered_df = df[(df["city"] == "Sydney") & (df["age"] > 30)]

    avg_salary = filtered_df["salary"].mean()

    print(f"Matching rows: {len(filtered_df):,}")
    print(f"Average salary: {avg_salary:,.2f}")


@benchmark
def polars_eager() -> None:
    df = pl.read_csv("users.csv")

    filtered_df = df.filter((pl.col("city") == "Sydney") & (pl.col("age") > 30))

    avg_salary = filtered_df["salary"].mean()

    print(f"Matching rows: {len(filtered_df):,}")
    print(f"Average salary: {avg_salary:,.2f}")


@benchmark
def polars_lazy() -> None:
    query = (
        pl.scan_csv("users.csv")
        .filter((pl.col("city") == "Delhi") & (pl.col("age") > 30))
        .select("salary")
        .mean()
        .explain()
    )

    print(query)


if __name__ == "__main__":
    # generate_csv()
    pandas_query()
    polars_eager()
    polars_lazy()
