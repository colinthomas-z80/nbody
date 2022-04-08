import numpy as np
import matplotlib.pyplot as plt
import time

def main():
    fig = plt.figure(figsize=(6,6), dpi=80)
    
    dt = 0.01
    pos = np.array([1, 2])
    vel = np.array([-.1, .25])

    for i in range(100):
        pos = np.add(pos, vel)
        vel += accel(pos, vel)*dt
        plt.cla()
        plt.scatter(2.5,2.5,s=25)
        plt.scatter(pos[0], pos[1], s=10)
        plt.xticks(np.arange(0,6))
        plt.yticks(np.arange(0,6))
        plt.pause(0.001)
        time.sleep(.1)
    plt.show()

def accel(pos, vel):
    center = np.array([2.5, 2.5])
    center_mass = 5

    dx = center[0] - pos[0]
    dy = center[1] - pos[1]
    nx = 0
    ny = 0
    
    if abs(dx) >= abs(dy):
        nx = dx/abs(dx)
        ny = dy/abs(dx)
    else:
        nx = dx/abs(dy)
        ny = dy/abs(dy)

    vec = np.array([nx, ny])
    return vec * center_mass


main()