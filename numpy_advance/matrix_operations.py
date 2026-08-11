import numpy as np


def main():

    ## Matrix Multiplication
    a = np.ones([9, 5, 7, 4])
    b = np.ones([9, 5, 4, 3])

    print(np.matmul(a, b).shape)

    ## Angle Calculation

    # Define your two vectors
    v1 = np.array([3, 4, 1])
    v2 = np.array([4, 1, 1])

    # Step 1: Compute the dot product
    dot_prod = np.dot(v1, v2)

    # Step 2: Compute the magnitudes (norms)
    mag_v1 = np.linalg.norm(v1)
    mag_v2 = np.linalg.norm(v2)

    # Step 3: Compute the cosine of the angle
    cos_theta = dot_prod / (mag_v1 * mag_v2)

    # Step 4: Protect against floating-point precision errors outside [-1.0, 1.0]
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    # Step 5: Get the angle in radians and convert to degrees
    angle_radians = np.arccos(cos_theta)
    angle_degrees = np.degrees(angle_radians)

    print(f"Angle in Radians: {angle_radians}")
    print(f"Angle in Degrees: {angle_degrees}")


if __name__ == "__main__":
    main()
