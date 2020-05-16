import numpy as np
import os
import sys
import math
import matplotlib.pyplot as plt
import random

from rrt_motion_prims import RRTMotionPrims

sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
                "/../RRTStar/")

from rrt_star import RRTStar

show_animation = True

class RRTPathSamples(RRTMotionPrims):
    def __init__(self, start, goal, obstacle_list, rand_area,
             max_iter=200,
             connect_circle_dist=50.0,
             precomputed_path = None
             ):
        super().__init__(start, goal, obstacle_list, rand_area, max_iter, connect_circle_dist)

        if precomputed_path:
            xx = []
            yy = []
            yaws = []
            for p1, p2 in zip(precomputed_path[:-1], precomputed_path[1:]):
                x1, y1 = p1
                x2, y2 = p2
                dx = x1 - x2
                dy = y1 - y2

                distance = math.sqrt((dx ** 2) + (dy ** 2))
                num_inc = int(np.round(distance / 0.2))

                xx_arr = np.linspace(x1, x2, num_inc)
                yy_arr = np.linspace(y1, y2, num_inc)
                xx += list(xx_arr)
                yy += list(yy_arr)

                theta = math.atan2(y1 - y2, x1 - x2)
                yaws += [theta for _ in xx_arr]
            yaws.append(goal[2])

        self.precomputed_path = list(zip(xx, yy, yaws))


    def get_random_node(self):
        if not self.precomputed_path:
            rnd = self.Node(random.uniform(self.min_rand, self.max_rand),
                random.uniform(self.min_rand, self.max_rand),
                random.uniform(-math.pi, math.pi)
                )
        else:
            x, y, yaw = random.choice(self.precomputed_path)
            x += random.uniform(-.5, .5)
            y += random.uniform(-.5, .5)
            yaw += random.uniform(-.5, .5)  
            rnd = self.Node(x, y, yaw)
        return rnd



def main(max_iter=200):
    print("Start " + __file__)

    # ====Search Path with RRT====
    # map 2
    # obstacleList = [
    #     (5, 5, 1),
    #     (3, 6, 2),
    #     (3, 8, 2),
    #     (3, 10, 2),
    #     (7, 5, 2),
    #     (9, 5, 2),
    #     (8, 10, 1),
    #     (6, 12, 1),
    # ]  # [x,y,size(radius)]

    # map 1
    obstacleList = [
        (5, 5, 1),
        (4, 6, 1),
        (4, 7.5, 1),
        (4, 9, 1),
        (6, 5, 1),
        (7, 5, 1),
        (8, 6, 1),
        (8, 7.5, 1),
        (8, 9, 1)
    ] 



    # Set Initial parameters
    start = [0.0, 0.0, np.deg2rad(90)]
    goal = [6.0, 7.0, np.deg2rad(90.0)]

    # rrt_star = RRTStar(start=start,
    #            goal=goal,
    #            obstacle_list=obstacleList, rand_area=[-2.0, 15.0], max_iter=max_iter)
    # first_path = rrt_star.planning(animation=True)
    # map 2
    # first_path = [[6.0, 7.0], [12.410825207200222, 8.700202423493208], [12.410825207200222, 8.700202423493208], [11.346624254534738, 3.8147673013832146], [8.639352029181408, 2.5222205525843857], [0.0, 0.0]]
    # map 1
    first_path = [[6.0, 7.0], [4.774040230480737, 11.520289665821362], [4.774040230480737, 11.520289665821362], [0.8954060098672572, 6.942495810405188], [0.0, 0.0], [0.0, 0.0]]
    print("first path: ", first_path)
    plt.plot([x for (x, y) in first_path], [y for (x, y) in first_path], '-r')
    plt.show()

    rrt_motion_prims = RRTPathSamples(start, goal,
                                              obstacleList,
                                              [-2.0, 15.0], max_iter=max_iter, precomputed_path=first_path)
    path = rrt_motion_prims.planning(animation=show_animation)
    # if path and show_animation:  # pragma: no cover
    #     rrt_star.draw_graph()
    #     plt.plot([x for (x, y) in path], [y for (x, y) in path], '-r')
    #     plt.grid(True)
    #     plt.pause(0.001)
    #     plt.show()
    #     Draw final path
    if path and show_animation:  # pragma: no cover
        rrt_motion_prims.draw_graph(title="RRT, path sampling, 200 iterations")
        plt.plot([x for (x, y, yaw) in path], [y for (x, y, yaw) in path], '-r')
        plt.grid(True)
        plt.pause(0.001)
        plt.show()


if __name__ == '__main__':
    main()