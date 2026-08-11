import numpy as np

# The Scalar Stretch (1D)


def scalarStretch(tax_value: float) -> None:
    base_price = np.array([1, 2, 3, 4, 5])
    print(base_price * tax_value)


# The Row Stretch (2D + 1D)


def rowStretch() -> None:
    batch_output = np.array(
        [[0.7, 0.9, 0.2], [0.1, 0.5, 0.8], [0.3, 0.6, 0.1], [0.4, 0.2, 0.9]]
    )

    bias_weights = [1, 1, 1]

    print(batch_output + bias_weights)


# The Cross-Hatch (Column vs. Row)


def crossHatch() -> None:
    originalArray = np.array([[0.7], [0.1], [0.9], [0.5]])
    batch_arr = np.array([1, 2, 3])
    print((originalArray + batch_arr).shape)


def main():
    scalarStretch(1.15)
    rowStretch()
    crossHatch()


if __name__ == "__main__":
    main()
