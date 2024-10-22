# b1-coding-practical-mt24
Coding practical task for the B1 Scientific Coding course at Oxford (MT24)

The task of this practical is to implement a controller to make a submarine track a reference in an underwater cave without hitting the cave floor/ ceiling.

Files:
mission.csv: contains the mission data

demo.ipynb: run this notebook to perform the mission, i.e. test the performance of the controller. Make changes to the controller gains here

best_gains.py: A script to calculate the best gains based on a cost function and a grid search. Run to print best K_P and K_D value for a particular mission.

control.py: Module containing controller class and compute_action method.

dynamic.py: Module containing modules for dynamic elements. Contains the Submarine, Trajectory, ClosedLoop and Mission classes.

terrain.py: Generates a reference trajectory and upper and lower limits for a given duration and scale. Contains the plot_reference_and_terrain method and the generate_reference_and_limits function.

