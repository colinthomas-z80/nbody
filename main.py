import numpy as np
import matplotlib.pyplot as plt
import time

def main():
    fig = plt.figure(figsize=(10,10), dpi=80)  
    plt.autoscale(False)
    dt = 0.03

    posr = np.random.randn(10000, 2)
    velr = np.random.randn(10000, 2)

    accr = accelr(posr)
    for i in range(10000):
        velr += accr * dt
        posr += velr * dt
        accr = accelr(posr)

        plt.cla()
        plt.scatter(posr[:, 0], posr[:, 1], s=10)
        plt.scatter(0,0,s=25)
        plt.xticks(np.arange(0,10))
        plt.yticks(np.arange(0,10))
        plt.xlim(-3, 3)
        plt.ylim(-3, 3)
        plt.pause(0.001)

    plt.show()

def accelr(posr):
    center = np.array([0, 0])
    center_mass = 1
    g = 2
    padding = 1

    dx = center[0] - posr[:,0:1] # this indexing is required to return as an hstack in the form [[x,y], [x,y], ....]
    dy = center[1] - posr[:,1:2]

    r = dx**2 + dy**2 + padding
    f = center_mass/r**2

    ax = f*g*dx*center_mass
    ay = f*g*dy*center_mass

    return np.hstack((ax, ay))

# def accel(pos, vel):
#     center = np.array([2.5, 2.5])
#     center_mass = 5

#     dx = center[0] - pos[0]
#     dy = center[1] - pos[1]
#     nx = 0
#     ny = 0
    
#     if abs(dx) >= abs(dy):
#         nx = dx/abs(dx)
#         ny = dy/abs(dx)
#     else:
#         nx = dx/abs(dy)
#         ny = dy/abs(dy)

#     vec = np.array([nx, ny])
#     return vec * center_mass


main()