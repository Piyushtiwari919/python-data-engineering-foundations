import pandas as pd


def main() -> None:
    df = pd.read_csv("datasets/results.csv")
    print(df.shape)
    print(df.info())


if __name__ == "__main__":
    main()
