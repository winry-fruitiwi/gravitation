# this is an object that makes a circle, or a sphere in 3D, that will orbit around
# an attractor.


class Star:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
    
    
    def apply_force(self, force): # force is a PVector.
        pass
    
    
    def show(self):
        pass
    
    
    def update(self):
        pass
