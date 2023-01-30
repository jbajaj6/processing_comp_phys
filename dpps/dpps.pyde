from Engine import *

ppm = 2 # pixels per meter
w = 600

def setup():
    size(w, 600)
    print("Key: " + str(ppm) + " pixels per meter")
    
    
def draw():
    global balls
    noStroke()
    background(101, 207, 240)
    fill(255)
    # frameRate(1/dt)
    scale(1, -1)
    translate(0, -height+100)
    noStroke()
    fill(86, 227, 86)
    rect(0, 0, width, -height)
    b = move()
    
    fill(255)
    fill(0)
    for ball in b:
        ellipse(ball.pos.x*ppm, ball.pos.y*ppm, 15, 15)
    ellipse(200*ppm, 0*ppm, 15, 15)
        
        
    
