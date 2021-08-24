# this attracts the other stars, or planets. This is what I think is a star.
from Star import *


class Attractor(Star):
    def __init__(self, x, y, z, m):
        super(Attractor, self).__init__(x, y, z, m)
    
    
    def attract(self, star): # star is a Star class, so it has a pos.x and pos.y!
        # using self.pos.sub() here would mutate the position, and we don't want that.
        distance = PVector.sub(self.pos, star.pos)
        # we'll want to restrain the strength soon
        # the gravitational constant will help us keep things in check
        G = 1
        # strength uses Newton's Universal Law of Gravitation. This is the key
        # of this project. F_g = G * m_1 * m_2/r^2
        
        # return zero if we're attracting ourselves
        try:
            strength = G * (self.m * star.m)/(distance.magSq())
        except ZeroDivisionError:
            return PVector(0, 0, 0)
        
        # The lower bound of constrain prevents things from drifting away, while the
        # higher bound prevents things from being launched into heaven
        strength = constrain(strength, 1, 2)
        return distance.setMag(strength)
    
    
    def show(self):
        pushMatrix()
        
        translate(self.pos.x, self.pos.y, self.pos.z)
        stroke(120, 80, 60, 80)
        fill(120, 80, 80, 80)
        sphere(self.m*2)
        
        popMatrix()
