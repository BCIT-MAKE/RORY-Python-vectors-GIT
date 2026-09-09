#BallScrewKneeVectors_v1
#Code to compute knee torque when using a ball screw actuator with lever arm. 
#Vector analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path
from vectoroperations import rotate2d

# %%
O=np.array([0,0]) #Knee center
P=np.array([0,0.05]) #Patella or lever arm middle position
L_lever=np.linalg.norm(P-O) #Lever arm length
L_pushrod=0.1 #Pushrod length from ballscrew

# Rotate2D(vector, angle in degrees CW +)
F = rotate2d(P, 180)*2   # foot vector









# %% Graphing
fig = plt.figure()
fig.canvas.manager.set_window_title('Ballscrewknee')
ax = plt.gca()

plt.quiver(O[0], O[1], P[0], P[1], angles='xy', scale_units='xy', scale=1, color='r', label='P')
plt.quiver(O[0], O[1], F[0], F[1], angles='xy', scale_units='xy', scale=1, color='b', label='F')
circle = patches.Circle((0, 0), radius=L_lever, edgecolor='black', facecolor='none', linewidth=0.2)
ax.add_patch(circle)

siz = 0.15
plt.xlim(-siz*2, siz*2)   # you often need to set limits manually —
plt.ylim(-siz, siz)   # quiver doesn't auto-scale the view the way plot() does
ax.set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
#plt.show()



# Use block in VSC to allow scrpit compeltion. not needed in Spyder. 
plt.show(block=False)
input("Press Enter to continue...")
plt.close('all')