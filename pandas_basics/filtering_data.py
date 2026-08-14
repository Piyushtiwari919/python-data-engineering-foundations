import pandas as pd


def main():
    df = pd.read_csv("datasets/Housing.csv")
    print(df)
    print(df.shape)
    print(df.columns)

    # Compound Filtering
    
    ## And
    print(df[(df["parking"] > 2) & (df["furnishingstatus"] == "furnished")])

    ## and - or
    print(
        df[
            (df["airconditioning"] == "yes")
            & ((df["stories"] == 2) | (df["area"] >= 5000))
        ]
    )
    
    column_selection = df.loc[:,["price","bedrooms","stories"]]
    
    print(column_selection)


if __name__ == "__main__":
    main()
