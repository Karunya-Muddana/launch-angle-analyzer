import math
import matplotlib.pyplot as plt

g = 9.8
t = float(input("Set a time period of the projectile motion --> "))

velocity = []
angles = []

for r in range(1, 101):  # r from 0 to 100 (inclusive)
    if r == 0:  # Use '==' for comparison, not '='
        u = 0
        angle = 90
        velocity.append(u)
        angles.append(angle)

    else:
        uInXdirection = r / t
        uInYdirection = (g * t) / 2

        usq = (uInXdirection ** 2) + (uInYdirection ** 2)
        u = math.sqrt(usq)

        angle_rad = math.atan(uInYdirection / uInXdirection)
        angle = math.degrees(angle_rad)
        
        velocity.append(u)
        angles.append(angle)

plt.plot(range(1, 101), velocity, color='blue')
plt.title("Initial Velocity vs Distance")
plt.xlabel("Distance (m)")
plt.ylabel("Initial Velocity (m/s)")
plt.grid(True)
plt.show()  

plt.plot(range(1, 101), angles, color='green')
plt.title("Launch Angle vs Distance")
plt.xlabel("Distance (m)")
plt.ylabel("Angle (degrees)")
plt.grid(True)
plt.show()  
