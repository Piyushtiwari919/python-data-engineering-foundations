import pandas as pd


ecommerse_data = pd.DataFrame(
    {
        "Region": [
            "North",
            "South",
            "East",
            "West",
            "South",
            "West",
            "East",
            "North",
            "East",
            "South",
            "West",
            "North",
            "East",
            "South",
            "West",
            "North",
            "East",
            "West",
            "East",
            "North",
            "South",
        ],
        "Sales_Rep": [
            "Vladimir Doe",
            "Sam Bahadur",
            "Jasen Huli",
            "Donald Pump",
            "John",
            "Aastha",
            "Yuli",
            "Ching Chong",
            "Ping Pong",
            "Ram",
            "Shyam",
            "Sita",
            "Gita",
            "Anita",
            "Babita",
            "Shivam",
            "Akash",
            "Vikash",
            "Golu",
            "Bholu",
            "Raju",
        ],
        "Revenue": [
            120101.00,
            132123.00,
            123654.00,
            111111.00,
            2739161.00,
            123456.00,
            132123.00,
            143214.00,
            176512.00,
            187676.00,
            678261.00,
            981121.00,
            432167.00,
            987676.00,
            761812.00,
            123456.00,
            279929.00,
            838393.00,
            484939.00,
            473929.00,
            1972919.00,
        ],
        "Units_Sold": [
            100,
            480,
            372,
            271,
            447,
            121,
            120,
            121,
            129,
            124,
            125,
            128,
            126,
            148,
            157,
            156,
            134,
            109,
            121,
            123,
            912,
        ],
    }
)


def main() -> None:
    df_group = ecommerse_data.groupby("Region").agg(
        {"Revenue": ["sum", "mean"], "Units_Sold": "max", "Sales_Rep": "count"}
    ).reset_index()
    print(df_group)


if __name__ == "__main__":
    main()
