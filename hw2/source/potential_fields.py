import numpy as np


class potential_fields:

    # Please complete these functions for question2, the arguments such as coefficient can be changed by your need. The return value should be a 2*1 matrix for robot to perform

    def uniform(self, vector=np.array([[1], [0]]), coefficient=1):
        return coefficient*vector

    def perpendicular(self, line_obstacle, car_position, coefficient=1):
        res = self.shortest_distance_point(
            line_obstacle[0], line_obstacle[1], car_position)
        return coefficient*(car_position-res[1])/pow(res[0], 3)

    def attractive(self, goal_point, car_position, coefficient=1):
        return coefficient*(goal_point-car_position)

    def repulsive(self, obstacle_point, car_position, coefficient=1):
        return coefficient*(car_position-obstacle_point)/pow(np.linalg.norm(car_position-obstacle_point), 3)

    def tangential(self, point, car_position, coefficient=1):
        vec = car_position-point
        n_vec = np.array([vec[0][0], vec[1][0], 0])
        perp = np.array([0, 0, -1])
        perp_vec = np.cross(n_vec, perp)
        res = np.array([[perp_vec[0]], [perp_vec[1]]])
        return coefficient*res

    def shortest_distance_point(self, v, w, p):
        # the minimum distance between line segment vw, and point p
        # v, w, p all are 2*1 matrix

        l2 = (w - v).T @ (w - v)
        if l2 == 0:
            return np.linalg.norm(p-v)

        t = max(0, min(1, (p - v).T @ (w - v) / l2))
        proj_point = v + t * (w-v)
        min_distance = np.linalg.norm(p-proj_point)

        return min_distance, proj_point, t
