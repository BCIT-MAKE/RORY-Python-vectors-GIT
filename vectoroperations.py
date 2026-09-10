#vectoroperations.py
#function to rotate a 2D vector by a given angle in degrees
import numpy as np

def rotate2d(v, angle_deg):
    theta = np.radians(angle_deg)
    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    return R @ v