import pandas as pd

house_data_dict = {
    "Property_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109],
    "Location": [
        "Malviya Nagar",
        "Greater Kailash",
        "Mayur Vihar",
        "Golf Links",
        "Sector 51",
        "Anand Vihar",
        "Sector 62",
        "Vasant Vihar",
        "Jor Bagh",
    ],
    "Raw_Price": [
        "$65000",
        "$110000",
        "$100000",
        "$95000",
        "$115000",
        "$70000",
        "$60000",
        "$80000",
        "$111000",
    ],
}


def main() -> None:

    # Conversion to Pyarrow for efficient data_handling

    df_using_dict = pd.DataFrame(house_data_dict)

    df_arrow_housing_data = df_using_dict.convert_dtypes(dtype_backend="pyarrow")

    print(df_arrow_housing_data.dtypes)

    # Price Cleanup (Vectorized String Operations with typecasting)
    clean_Price_USD = (
        df_arrow_housing_data["Raw_Price"].str.replace("$", "").astype(float)
    )

    # Printing Converted column
    print(clean_Price_USD)

    # Checking the data type
    print(clean_Price_USD.dtypes)


if __name__ == "__main__":
    main()
