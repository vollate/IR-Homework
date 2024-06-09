"""

This script implements a multilateration algorithm that, given the coordinates of a finite number of radio stations,
and given their distances to the station (derived from the intensities of the signal they received in a previous step)
computes the most probable coordinates of the station. Even if the distances computed for each station do not match
(in terms of pointing to a single optimal solution) the algorithm finds the coordinates that minimize the error function
and returns the most optimal solution possible.


https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
https://docs.scipy.org/doc/scipy/reference/optimize.minimize-neldermead.html#optimize-minimize-neldermead

"""

from scipy.optimize import minimize
from cmaes import CMA
import numpy as np


def quadratic(x, c, r):

    '''
    complete the error section for task2
    x: point
    c: stations (APs)
    r: distance_to_station (d)
    '''

    # ----------------------task2----------------------

    error = 0
    for ci, ri in zip(c, r):
        error += (np.linalg.norm(x - ci) - ri) ** 2

    # ----------------------task2----------------------



    return error


if __name__ == "__main__":
    stations = list(np.array([[1, 1], [0, 1], [1, 0], [0, 0]]))
    distance_to_station = [0.1, 0.5, 0.5, 1.3]
    # optimizer = CMA(mean=np.zeros(2), sigma=1.3)

    '''
    complete the main function for task3
    '''

    # ----------------------task3----------------------

    optimizer = CMA(mean=np.zeros(2), sigma=1.3, population_size=10)

    # Run the optimization
    best_solution = None
    best_value = float('inf')
    generation = 0
    while True:
        solutions = []
        for _ in range(optimizer.population_size):
            x = optimizer.ask()
            value = quadratic(x, stations, distance_to_station)
            solutions.append((x, value))
            if value < best_value:
                best_value = value
                best_solution = x
        optimizer.tell(solutions)

        # Print the best solution in the current generation
        print(f"Generation {generation}: Best solution = {best_solution}, Best value = {best_value}")

        # Check convergence criteria or limit the number of generations
        generation += 1
        if generation >= 100:  # Limit to 100 generations for this example
            break

    # Get the final best solution
    print("Estimated position:", best_solution)
    # ----------------------task3----------------------



