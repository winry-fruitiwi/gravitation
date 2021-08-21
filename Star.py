# this is an object that makes a circle, or a sphere in 3D, that will orbit around
# an attractor.


class Star(object):
    def __init__(self, x, y, m):
        self.pos = PVector(x, y)
        self.vel = PVector(0, 10)
        self.acc = PVector(0, 0)
        self.m = m
        self.ms = random(10, 15) # max speed prevents things from getting lightfast!
        print "We made a star!"
    
    
    def apply_force(self, force): # force is a PVector.
        # F = ma, so a = F/m.
        self.acc.add(force).div(self.m)
    
    
    def show(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        
        noStroke()
        fill(0, 0, 100, 80)
        circle(0, 0, self.m*2)
        
        popMatrix()
    
    
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.acc).limit(self.ms)
        self.acc = PVector(0, 0)
