import pgzrun
import sys
HEIGHT = 600
WIDTH = 800

quad = Actor('quadrado.png')
quad.pos = 300,200
quad.velocity = 1.6


base = Actor('base.png')
base.pos = 400,600

def draw():
    screen.clear()
    quad.draw()
    base.draw()

def update():
    quad.x += 1
    if not quad.colliderect(base):
        quad.y += quad.velocity
    if quad.x > WIDTH+quad.width or quad.y > HEIGHT+quad.height:
            sys.exit()

pgzrun.go()