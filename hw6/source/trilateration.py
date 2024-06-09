import numpy as np


def trilateration(distances_to_APs, STA_coordinates):
    x1, y1 = STA_coordinates[0]
    x2, y2 = STA_coordinates[1]
    x3, y3 = STA_coordinates[2]

    d1, d2, d3 = distances_to_APs

    A = np.array([
        [2 * (x1 - x3), 2 * (y1 - y3)],
        [2 * (x2 - x3), 2 * (y2 - y3)]
    ])

    b = np.array([
        x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2 + d3 ** 2 - d1 ** 2,
        x2 ** 2 - x3 ** 2 + y2 ** 2 - y3 ** 2 + d3 ** 2 - d2 ** 2
    ])

    X = np.linalg.lstsq(A, b, rcond=None)[0]

    return X


if __name__ == "__main__":
    stations = np.array([[1, 1], [0, 1], [1, 0]])
    distances_to_station = [0.1, 0.5, 0.5]
    position = trilateration(distances_to_station, stations)
    print("Estimated position:", position)
