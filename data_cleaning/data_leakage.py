import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

house_mock_data = {
    "Square_Footage": [
        1600,
        np.nan,
        2000,
        2100,
        1500,
        3250,
        np.nan,
        3000,
        2450,
        np.nan,
        2150,
        5000,
        490,
        1000,
        4100,
        3210,
        7000,
        np.nan,
        2300,
        8000,
    ],
    "Price": [
        1900000,
        2100000,
        2500000,
        2300000,
        1700000,
        4000000,
        3000000,
        1800000,
        3000000,
        1000000,
        2000000,
        5000000,
        500000,
        1200000,
        4000000,
        3000000,
        7000000,
        3400000,
        2400000,
        8100000,
    ],
}


def main() -> None:

    ## The Data Leakage

    df_housing_data = pd.DataFrame(house_mock_data)
    df_arrow_Housing_Data = df_housing_data.convert_dtypes(dtype_backend="pyarrow")

    global_mean_sqaure_footage = df_arrow_Housing_Data["Square_Footage"].mean()
    print("Leaked Global mean :", global_mean_sqaure_footage)

    ## The Efficient Way

    X = df_arrow_Housing_Data["Square_Footage"]
    y = df_arrow_Housing_Data["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # print(X_train, X_test, y_train, y_test)

    mean_square_footage = X_train.mean()
    print(f"Isolated Training Mean: {mean_square_footage}")

    X_train = X_train.fillna(mean_square_footage)

    X_test = X_test.fillna(mean_square_footage)

    # print(X_train, X_test)
    
    ## Note :- We use a SimpleImputer inside a pipeline rather than manually calculating and filling the mean


if __name__ == "__main__":
    main()
