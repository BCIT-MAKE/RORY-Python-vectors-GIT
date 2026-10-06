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

# function to find third point of triangle given 2 points and 3 side lengths. 
# Inputs:  P (patella point) and OB, pivot point fo the second lever arm. Length of the second lever arm and coupler rod
def triangle3rdpoint(P,OB,LB_coupler,LB_lever):

    # Calculate the distance between the two known points
    OB2Pvec=P-OB
    LB_OB2Pvec = np.linalg.norm(OB2Pvec, axis=0)


    # Check if a triangle can be formed with the given side lengths
    invalid = (LB_OB2Pvec > (LB_coupler + LB_lever)) | (LB_OB2Pvec < abs(LB_coupler - LB_lever))
    if np.any(invalid):
        raise ValueError("The given lengths do not form a valid triangle for at least one angle in the sweep.")


    dir_OB2Pvec = OB2Pvec / LB_OB2Pvec  # Unit vector from OB to P
    ver_OB2Pvec = np.array([-dir_OB2Pvec[1], dir_OB2Pvec[0]])  # Perpendicular unit vector

    Lx=(LB_lever**2+LB_OB2Pvec**2 - LB_coupler**2) / (2 * LB_OB2Pvec)
    Ly=np.sqrt(LB_lever**2 - Lx**2)

    PBvec = OB + Lx * dir_OB2Pvec + Ly * ver_OB2Pvec


    return PBvec