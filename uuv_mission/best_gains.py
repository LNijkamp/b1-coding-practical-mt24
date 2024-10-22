import sys
import os
# Add the parent directory of uuv_mission to the Python path
sys.path.append(os.path.abspath('/Users/lukenijkamp/Library/CloudStorage/OneDrive-Nexus365/Engineering 3rd year/B1 Engineering Computation/Scientific coding/B1 Practical 1/b1-coding-practical-mt24'))

import numpy as np
from uuv_mission.dynamic import Submarine, ClosedLoop, Mission
from uuv_mission.control import Controller
from uuv_mission.terrain import generate_reference_and_limits

# Define a cost function to evaluate the performance
def cost_function(reference, trajectory):
    return np.mean((reference - trajectory) ** 2)

# Define a range of values for K_P and K_D
K_P_values = np.linspace(0.0, 1.0, 20)
K_D_values = np.linspace(0.0, 1.0, 20)

# Load the mission
mission = Mission.from_csv("/Users/lukenijkamp/Library/CloudStorage/OneDrive-Nexus365/Engineering 3rd year/B1 Engineering Computation/Scientific coding/B1 Practical 1/b1-coding-practical-mt24/data/mission.csv")

best_cost = float('inf')
best_K_P = None
best_K_D = None

# Grid search for the best K_P and K_D
for K_P in K_P_values:
    for K_D in K_D_values:
        sub = Submarine()
        controller = Controller(K_P, K_D)
        closed_loop = ClosedLoop(sub, controller)
        trajectory = closed_loop.simulate_with_random_disturbances(mission)
        
        # Calculate the cost
        cost = cost_function(mission.reference, trajectory.position[:, 1])  # Assuming y-position is the relevant metric
        
        if cost < best_cost:
            best_cost = cost
            best_K_P = K_P
            best_K_D = K_D

print(f"Best K_P: {best_K_P}, Best K_D: {best_K_D}")

# Use the best gains to simulate the final trajectory
sub = Submarine()
controller = Controller(best_K_P, best_K_D)
closed_loop = ClosedLoop(sub, controller)
trajectory = closed_loop.simulate_with_random_disturbances(mission)
trajectory.plot_completed_mission(mission)