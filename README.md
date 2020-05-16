## Project Overview
 Our project is a survey of sample-based planning for non-holonomic systems. This website provides an overview of our work, along with more detailed experimentation results. 
 
### Abstract
We review a breadth of literature related to non-holonomic motion planning methods, then provide a deep analysis of current solutions to near-optimal sample-basedplanning with obstacles with the RRT* algorithm. We suggest a method for achieving the desirable properties of RRT* whileachieving dynamical feasibility of generated paths in non-holonomic systems

## Literature Review


## Experimentation and Results
To demonstrate potential advantages of different approaches to dynamically-feasible path planning around obstacles for non-holonomic systems, we implemented some of the algorithms we found during review and compared the results qualitatively. Our simulations were created by extending the RRT implementations within the Python Robotics package.

We were especially interested in planners that can navigate around obstacles, so we chose two layouts to run our tests on.
1. Placing the goal within a U-shaped obstacle so that the agent needs to find the opening of the U
2. Positioning obstacles that require the agent to navigate through narrow openings to reach the goal

We began with a basic implementation of RRT with motion primitives, uniformly sampling the space. This is the initial set of motion primitives we used:

<img src="media/motionprimtives.png" alt="motion primitives"
	width="450"/>

Sample result after running RRT for 200 iterations:

<img src="media/uniformsampling_2.gif" alt="200 iterations of RRT"
	width="450"/>

<img src="media/rrtmap1.png" alt="Result image"
	width="450"/>

Next, we turned to path-biased sampling approaches. These entail first pre-generating a dynamically infeasible path and then running RRT, biasing samples towards points along the pre-generated path. 

## Team Bios
### Rebecca Abraham
Rebecca is a 4th year undergraduate student at UC Berkeley studing Electrical Engineering & Computer Science. Rebecca is an undergraduate research fellow at the Berkeley Center for New Media.

### Evan Lohn


