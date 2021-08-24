# based on Daniel's Mutual Gravitation video in p5.js
# v0.00:   blank project with these version comments
# v0.01:   basic mover class with main program shell, possibly edge check
# v0.02:   fill in mover class, edge check optional
# v0.03:   attractor, maxspeed
# v0.04:   repulsor that inherits attractor
# v0.05:   mutual gravitation
# v0.0:    try to add P3D, Peasycam, and 3D gravitation with path tracing
# v0.0:    colors!

# in order to use the PeasyCam object, I need to add the library! Note: cam.startHUD()
# and cam.stopHUD() or perhaps cam.endHUD() is the way to make 2D items in 3D.
from Star import *
from Attractor import *
from Repulsor import *
add_library("peasycam")


def setup():
    global stars, attractors, repulsors # ignore the second two items
    colorMode(HSB, 360, 100, 100, 100)
    size(950, 1000, P3D)
    background(220, 79, 35)
    stars = []
    attractors = []
    repulsors = []
    cam = PeasyCam(this, 0, 0, 0, 500)
    
    '''
    for i in range(8):
        # stars.append(Star(random(80, width-80), random(10, height-10), random(2, 15)))
        stars.append(Star(random(100, width-100), random(100, height-100), random(5, 15)))
    '''
    
    # for i in range(1):
    #     attractors.append(Attractor(width/2, height/2, random(8, 16)))


def draw_axes():
    strokeWeight(1)
    # x-axis
    stroke(0, 80, 80, 100)
    line(-4000, 0, 4000, 0)
    
    # y-axis
    stroke(120, 80, 80, 100)
    line(0, -4000, 0, 4000)
    
    # z-axis
    stroke(201, 80, 80, 100)
    line(0, 0, -4000, 0, 0, 4000)


def star_update():
    for star in stars:
        star.show()
        star.update()
        # star.apply_force(gravity)
        for attractor in attractors:
            star.apply_force(attractor.attract(star))
            attractor.show()
        
        for repulsor in repulsors:
            star.apply_force(repulsor.repulse(star))
            repulsor.show()


def draw():
    global stars, attractors, repulsors
    background(220, 79, 35)
    draw_axes()
    gravity = PVector(0, 0.1)
    
    
    for i in range(len(attractors)):
        # list[~i] is the same as list[i]!
        for attracted_attractor in attractors:
            attractor = attractors[i]
            attracted_attractor.apply_force(attractor.attract(attracted_attractor))
            attractor.show()
            attractor.update()


def keyPressed():
    global attractors, repulsors, stars
    
    # add a star!
    R = 100 # r is our radius for adding stars near the origin
    if key == "a": 
        attractors.append(Attractor(random(-R, R),
                                    random(-R, R),
                                    random(-R, R),
                                    random(8, 16)))
    
    # if mouseButton == RIGHT:
    #     repulsors.append(Repulsor(mouseX, mouseY, random(8, 16)))
    
    # for i in range(3):
    #     stars.append(Star(random(100, width-100), random(100, height-100), random(5, 15)))
