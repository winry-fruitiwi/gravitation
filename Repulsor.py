# this is the same as Attractor, except it repulses instead.
from Attractor import *


class Repulsor(Attractor):
    # We don't even need an __init__() because everything is already inherited!
    # assume star is a Star object. This is the opposite of attract.
    def repulse(self, star): 
        return self.attract(star).mult(-1)
    
    
    def show(self):
        pushMatrix()
        
        translate(self.pos.x, self.pos.y)
        fill(0, 80, 80, 80)
        circle(0, 0, self.m*2)
        
        popMatrix()
