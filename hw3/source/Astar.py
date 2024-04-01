import numpy as np
import queue
from math import sqrt


class Astar:
    def __init__(self):
        # graph node: x, y, cost, parent
        self.cur_vis = []  # current visited node list
        self.next_vis = []  # next visit node list

    def find_path(self, graph, start_pos, goal_pos):

        '''
        graph: the instance of the class defined in the grid_graph file
        start_pos: The start node consist of four parts: (x, y, cost, parent node)
        goal_pos: The goal node consist of four parts: (x, y, cost, parent node) 
        '''

        print('start to Astar search')

        frontier = queue.PriorityQueue()  # priority queue for algorithm to explore current points.
        frontier.put((self.heuristic(start_pos, goal_pos), start_pos))  # put the priority and position
        cost_so_far = np.zeros((graph.width, graph.height))  # cost matrix from start point to this point
        final_node = None

        while not frontier.empty():
            _, cur = frontier.get()
            if graph.node_equal(cur, goal_pos):
                final_node = cur
                break
            if [cur.x, cur.y] in self.cur_vis:
                continue
            self.cur_vis.append([cur.x, cur.y])
            for neighbor in graph.neighbors(cur):
                new_cost = cost_so_far[cur.x, cur.y] + neighbor.cost
                if [neighbor.x, neighbor.y] not in self.cur_vis and [neighbor.x, neighbor.y] not in self.next_vis:
                    new_cost = cost_so_far[cur.x, cur.y] + neighbor.cost
                    cost_so_far[neighbor.x][neighbor.y] = new_cost
                    frontier.put((new_cost + self.heuristic(neighbor, goal_pos), neighbor))
                elif [neighbor.x, neighbor] in self.next_vis:
                    if new_cost < cost_so_far[neighbor.x][neighbor.y]:
                        cost_so_far[neighbor.x][cost_so_far.y] = new_cost
                        frontier.put(new_cost + self.heuristic(neighbor, goal_pos), neighbor)
            # please complete this part for the homework question1
            # each node has four parts: x position, y position, the cost so far, the parent node. Utilize the parent node, the path can be generated

            # parts: (1) get current node with priority (using frontier.get()[1])
            # (2) check whether current node is the goal node (using graph.node_equal)
            # (3) explore the neighbors of current node (using graph.neighbors)
            # (4) if the neighbor node is not in the next_vis (and cur_vis): put that in the frontier with priority and append that in the next_vis.  (priority= cost_so_far + heuristic)
            # (5) if the neighbor node is in the next_vis: check whether cost so far is less than that in the next_vis to determine whether put it in the frontier
            # (6) return the node when it is in the goal position.
        print('search done')
        return final_node, self.cur_vis

    def heuristic(self, node1, node2, coefficient=5):
        # please complete the heuristic function for the homework question1  (related to the distance to the goal)
        return coefficient * pow((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2, 2)

    def generate_path(self, final_node):
        # utilize the node to generate the path. 

        path = [[final_node.x, final_node.y]]

        while final_node.parent is not None:
            path.append([final_node.parent.x, final_node.parent.y])
            final_node = final_node.parent

        return path
