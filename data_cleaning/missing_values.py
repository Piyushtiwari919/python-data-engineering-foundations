import pandas as pd


def main() -> None:
    # missing values
    df = pd.read_csv("datasets/employees.csv", dtype_backend="pyarrow")

    # filling missing values with zero
    df = df.fillna(0)

    missing_values = df.isnull()
    print(missing_values)


if __name__ == "__main__":
    main()
