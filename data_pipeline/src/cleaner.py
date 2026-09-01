import csv
import random
import json
import pandas as pd


"""
# Generating CSV File

OUTPUT_FILE = "users.csv"

NUM_ROWS = 100000

first_names = [
    "Aarav",
    "Vivaan",
    "Aditya",
    "Vihaan",
    "Arjun",
    "Sai",
    "Reyansh",
    "Ayaan",
    "Krishna",
    "Ishaan",
    "Diya",
    "Sanya",
    "Aanya",
    "Aadhya",
    "Ananya",
    "Pari",
    "Riya",
    "Navya",
    "Meera",
    "Kavya",
]
last_names = [
    "Sharma",
    "Verma",
    "Gupta",
    "Malhotra",
    "Bansal",
    "Aggarwal",
    "Singh",
    "Kumar",
    "Mehra",
    "Joshi",
    "Patel",
    "Reddy",
    "Rao",
    "Nair",
    "Iyer",
]
domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com", "mail.com"]

nan_probability = 0.05


def generate_csv():
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "email"])
        for _ in range(NUM_ROWS):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            name = f"{first_name} {last_name}"
            age = random.randint(1, 99)
            email = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 999)}@{random.choice(domains)}"

            final_name = "" if nan_probability > random.random() else name
            final_age = "" if nan_probability > random.random() else age
            final_email = "" if nan_probability > random.random() else email

            writer.writerow([final_name, final_age, final_email])
        print(f"Generated {NUM_ROWS:,} rows in {OUTPUT_FILE}")

"""

"""
# Creating RAW JSON FILE

def generate_json():
    for i in range(1, 11):
        data = {
            "user_id": random.randint(1, 100) + i,
            "name": f"user_{i}",
            "subscription_status": random.choice(["active", "expired"]),
        }

        file_name = f"file_{i}.json"

        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)

"""


def clean_user_csv():
    df = pd.read_csv("data/raw/users.csv", dtype_backend="pyarrow")
    median_age = df["age"].median()
    df = df.fillna({"age": median_age})
    df = df.dropna(subset=["email", "name"])
    df["email"] = df["email"].str.lower()
    return df


# def main() -> None:

#     clean_user_csv()

#     # generate_csv()
#     # generate_json()


# if __name__ == "__main__":
#     main()
