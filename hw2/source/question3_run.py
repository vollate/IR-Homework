import numpy as np
from ir_sim.env import EnvBase
from ir_sim.util.collision_dectection_geo import collision_seg_seg
from potential_fields import potential_fields
from collections import namedtuple
import argparse

parser = argparse.ArgumentParser(
    description='The given force potential fields')
parser.add_argument('-a', '--animation', action='store_true')
args = parser.parse_args()

point = namedtuple('point', 'x y')

env = EnvBase(world_name='question3.yaml', save_ani=args.animation)

pf = potential_fields()

line_obs = env.get_obstacle_list()


def in_range_check(robot_state, line_obs):
    if abs(line_obs.points[0][0] - line_obs.points[1][0]) < 0.1:
        min_y = min(line_obs.points[0][1], line_obs.points[1][1]) - 0.9
        max_y = max(line_obs.points[0][1], line_obs.points[1][1]) + 0.9
        res = max_y > robot_state[1][0] > min_y
    else:
        min_x = min(line_obs.points[0][0], line_obs.points[1][0]) - 0.9
        max_x = max(line_obs.points[0][0], line_obs.points[1][0]) + 0.9
        res = max_x > robot_state[0][0] > min_x
    return res


def check_intersection(line1_start, line1_end, line2_start, line2_end):
    line2_direction = line2_end - line2_start
    line2_direction_unit = line2_direction / np.linalg.norm(line2_direction)

    line2_start = line2_start - 0.9 * line2_direction_unit
    line2_end = line2_end + 0.9 * line2_direction_unit

    line1_vec = line1_end - line1_start
    line2_vec = line2_end - line2_start

    def cross_call(v1, v2):
        return v1[0] * v2[1] - v1[1] * v2[0]

    d1 = cross_call(line2_vec, line1_start - line2_start)
    d2 = cross_call(line2_vec, line1_end - line2_start)
    d3 = cross_call(line1_vec, line2_start - line1_start)
    d4 = cross_call(line1_vec, line2_end - line1_start)

    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    return False


for i in range(1000):
    # please complete this part to solve question3 based on the force defined in question2
    f_repulsive = np.array([[0.0], [0.0]])
    f_attractive = np.array([[0.0], [0.0]])
    f_tangential = np.array([[0.0], [0.0]])
    no_collision = True
    forces = []
    for obs in line_obs:
        forces.append(pf.perpendicular(line_obstacle=obs.points, car_position=env.robot.state,
                                       coefficient=10 if in_range_check(env.robot.state, obs) else 0))
        if check_intersection(env.robot.state,
                              env.robot.goal,
                              obs.points[0],
                              obs.points[1]):
            no_collision = False
    if not no_collision:
        for force in forces:
            f_repulsive += force

    f_tangential = pf.tangential(point=env.robot.goal, car_position=env.robot.state,
                                 coefficient=0.7 if not no_collision else 0)
    f_attractive = pf.attractive(
        goal_point=env.robot.goal, car_position=env.robot.state, coefficient=0.5)

    pf_force = f_repulsive + f_attractive + f_tangential

    # please complete this part to solve question3 based on the force defined in question2

    env.step(pf_force)
    env.render(show_traj=True)

    if env.done():
        break

env.end(ani_name='potential_field', ani_kwargs={'subrectangles': True})
