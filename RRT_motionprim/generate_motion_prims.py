import copy
import math
import os
import random
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
                "/../ReedsSheppPath/")

from reeds_shepp_path_planning import generate_local_course

def path_params():
	ret = []
	for l in [-.1, .1]:
		for m in ['S', 'L', 'R']:
			for c in [1,]:
				ret.append((l, m, c))
	print(ret)
	return ret

def main():
	fig, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
	fig.suptitle('Hierarchical Motion Primitives')

	px, py, pyaw, directions = generate_local_course(1.0, [1.0], ['L'], 1.0, 0.01)
	for l, m, c in path_params():
			px, py, pyaw, directions = generate_local_course(abs(l * c), [l * c], [m], c, c * 0.01)
			ax1.plot(px, py)
	ax1.set_title("Level 0")

	for l1, m1, c1 in path_params():
		for l2, m2, c2 in path_params():
			px, py, pyaw, directions = generate_local_course(abs(l1 * c1) + abs(l2 * c2), [l1 * c1, l2 * c2], [m1, m2], c1, c1 * 0.01)
			ax2.plot(px, py)
	ax2.set_title("Level 1")
	plt.show()



if __name__ == '__main__':
    main()