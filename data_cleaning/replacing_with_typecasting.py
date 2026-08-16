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

    df_using_dict = pd.DataFrame(house_data_dict)

    ## Slow -> Using Iterrows :-]
    
    cleaned_prices = []

    for index, row in df_using_dict.iterrows():
        clean_val = float(str(row["Raw_Price"]).replace("$", ""))
        cleaned_prices.append(clean_val)

    # Putting column to the dataframe
    # df_using_dict["clean_Price_USD"] = cleaned_prices

    ## Fast -> Using Vectorized String Operations

    df_arrow_housing_data = df_using_dict.convert_dtypes(dtype_backend="pyarrow")
    print(df_arrow_housing_data.dtypes)

    # Price Cleanup (Vectorized String Operations with typecasting)
    df_arrow_housing_data["clean_Price_USD"] = (
        df_arrow_housing_data["Raw_Price"].str.replace("$", "").astype(float)
    )

    # Printing Converted data
    print(df_arrow_housing_data)

    # Checking the data type
    print(df_arrow_housing_data["clean_Price_USD"].dtypes)


if __name__ == "__main__":
    main()
