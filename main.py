import numpy as np
import matplotlib.pyplot as plt
import time

def main():
    fig = plt.figure(figsize=(3,3), dpi=80)  
    dt = 0.01

    posr = np.random.randn(10, 2)
    velr = np.random.randn(10, 2)

    accr = accelr(posr)
    for i in range(10000):
        velr += accr * dt
        posr += velr * dt
        accr = accelr(posr)

        plt.cla()
        plt.scatter(posr[:, 0], posr[:, 1], s=10)
        plt.scatter(2.5,2.5,s=25)
        plt.xticks(np.arange(0,6))
        plt.yticks(np.arange(0,6))

        plt.pause(0.001)

    plt.show()

def accelr(posr):
    center = np.array([2.5, 2.5])
    center_mass = 5
    g = 2

    dx = center[0] - posr[:,0:1] # this indexing is required to return as an hstack in the form [[x,y], [x,y], ....]
    dy = center[1] - posr[:,1:2]

    r = dx**2 + dy**2
    f = center_mass/abs(r)

    ax = f*g*dx*center_mass
    ay = f*g*dx*center_mass

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