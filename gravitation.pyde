# based on Daniel's Mutual Gravitation video in p5.js
# v0.0:   blank project with these version comments
# v0.0:   basic mover class with main program shell, possibly edge check
# v0.0:   fill in mover class, edge check optional
# v0.0:   attractor
# v0.0:   repulsor that inherits attractor
# v0.0:   mutual gravitation
# v0.0:   path tracing
# v0.0:   emittion, get particles and/or trail
# v0.0:   try to add P3D, Peasycam, and 3D gravitation with path tracing
# v0.0:   colors!
from Star import *


def setup():
    global stars, attractors, repulsors # ignore the second two items
    colorMode(HSB, 360, 100, 100, 100)
    size(950, 1000)
    background(220, 79, 35)
    stars = []
    
    for i in range(1):
        stars.append(Star(width/2, height/2))
    
    attractors = []
    repulsors = []


def draw():
    global stars, attractors, repulsors
    background(220, 79, 35)
    gravity = PVector(0, 1)
    
    for star in stars:
        star.show()
        star.update()
        star.apply_force(gravity)
