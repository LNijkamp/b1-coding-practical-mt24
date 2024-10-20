import numpy as np

class Controller:
    def __init__(self, K_P: float, K_D: float):
        self.K_P = K_P
        self.K_D = K_D
        self.previous_error = 0.0

    def compute_action(self, observation: float, reference: float) -> float:
        # Compute the current error
        error = reference - observation
        
        # Compute the change in error
        error_change = error - self.previous_error
        
        # Compute the control action
        action = self.K_P * error + self.K_D * error_change
        
        # Update the previous error
        self.previous_error = error
        
        return action