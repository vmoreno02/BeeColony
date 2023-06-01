"""Functions for a vector in polar coordinates"""
"""angles stored in radians"""

import math

class Vector:
    def __init__(self, r, theta) -> None:
        self.r = r
        self.theta = theta

    def add(self, vec):
        x = (self.r * math.cos(self.theta)) + (vec.r * math.cos(self.theta))
        y = (self.r * math.sin(self.theta)) + (vec.r * math.sin(self.theta))

        r_new = math.hypot(x, y)
        theta_new = math.atan(y / x)

        return Vector(r_new, theta_new)
    
    def get_reverse_unit_vec(self):
        theta_new = (self.theta + math.pi) % (2 * math.pi) # accounts for going over 2pi or under 0
        r_new = 1
        return Vector(r_new, theta_new)
    
    def get_cartesian(self):
        x = self.r * math.cos(self.theta)
        y = self.r * math.sin(self.theta)
        return x, y
    
    def print(self) -> str:
        s = "r: " + str(self.r) + ", theta: " + str(self.theta)
        return s
    
if __name__ == "__main__":
    vec = Vector(1, math.pi + 1)
    print(vec.print())
    new_vec = vec.get_reverse_unit_vec()
    print(new_vec.print())