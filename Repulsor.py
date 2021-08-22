# this is the same as Attractor, except it repulses instead.
from Attractor import *


class Repulsor(Attractor):
    def __init__(self, x, y, m):
        super(Repulsor, self).__init__(x, y, m)
    
    
    def repulse(self, star): # assume star is a Star object. Confusing!
        return self.attract(star).mult(-1)
    
    
    def show(self):
        pushMatrix()
        
        translate(self.pos.x, self.pos.y)
        fill(0, 80, 80, 80)
        circle(0, 0, self.m*2)
        
        popMatrix()
