# this is an object that makes a circle, or a sphere in 3D, that will orbit around
# an attractor.


class Star(object):
    def __init__(self, x, y, m):
        self.pos = PVector(x, y)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.m = m
        self.max_speed = 4 # max speed prevents things from getting lightfast!
        # print "We made a star!"
    
    
    # force is a PVector. This is the most boring part of the Star class.
    def apply_force(self, force):
        # F = ma, so a = F/m.
        # self.acc.add(force).div(self.m)
        self.acc.add(PVector.div(force, self.m))
    
    
    def show(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        
        noStroke()
        fill(0, 0, 100, 80)
        circle(0, 0, self.m*2)
        
        popMatrix()
    
    
    # this updates the object's attributes. This is probably the second most boring part
    # of the implementation.
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.acc).limit(self.max_speed)
        self.acc = PVector(0, 0)
