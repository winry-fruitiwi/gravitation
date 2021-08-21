# this attracts the other stars, or planets. This is what I think is a star.
from Star import *


class Attractor(Star):
    def __init__(self, x, y, m):
        super(Attractor, self).__init__(x, y, m)
        print "we made an attractor at " + str(self.pos)
        self.vel = PVector(0, 0)
    
    
    def attract(self, star): # star is a Star class, so it has a pos.x and pos.y!
        # using self.pos.sub() here would mutate the position, and we don't want that.
        distance = PVector.sub(self.pos, star.pos)
        # we'll want to restrain the strength soon
        # the gravitational constant will help us keep things in check
        G = 10
        # strength uses Newton's Universal Law of Gravitation. This is the key
        # of this project. F_g = G * m_1 * m_2/r^2
        strength = G * (self.m * star.m)/(distance.magSq())
        strength = constrain(strength, 10, 30)
        return distance.setMag(strength)
    
    
    def show(self):
        pushMatrix()
        
        translate(self.pos.x, self.pos.y)
        fill(120, 80, 80, 80)
        circle(0, 0, self.m*2)
        
        popMatrix()
