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

# this rotate function can take an anglesweep vector isntead of just a single value.
def rotate2dsweep(v, angle_deg):
    theta = np.radians(angle_deg)
    c, s = np.cos(theta), np.sin(theta)
    x = v[0]*c - v[1]*s
    y = v[0]*s + v[1]*c
    return np.array([x, y])
