import numpy as np


def main():
    # Initialize the generator
    rng = np.random.default_rng()
    
    random_int_arr = rng.integers(low=1, high=100, size=100)

    random_float_arr = rng.uniform(low=1.0, high=100.0, size=(10, 10))

    print(random_int_arr[(random_int_arr > 50) & (random_int_arr < 80)])
    print(random_float_arr[(random_float_arr > 50) & (random_float_arr < 80)])


if __name__ == "__main__":
    main()
