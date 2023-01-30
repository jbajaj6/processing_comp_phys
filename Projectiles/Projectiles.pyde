from Physics_Engine import *

ppm = 1.5 # pixels per meter
w = 600

clouds = []
num_clouds = int(random(2, 6))
for i in range(num_clouds):
    y = random(50, 250)
    clouds.append([i * ((w-90)/num_clouds) + 90, y, i * ((w-90)/num_clouds) + 90])


def setup():
    size(w, 600)
    print("Key: " + str(ppm) + " pixels per meter")
    
    
def draw():
    noStroke()
    background(101, 207, 240)
    fill(255)
    for i in clouds:
        ellipse(i[0], i[1], 70, 70)
        ellipse(i[2], i[1] + 20, 120, 40)
    frameRate(1/dt)
    scale(1, -1)
    translate(0, -height+100)
    noStroke()
    fill(86, 227, 86)
    rect(0, 0, width, -height)
    move()
    
    fill(255)
    for i in pp:
        ellipse(i.x*ppm, i.y*ppm, 10, 10)
    fill(0)
    ellipse(p.x*ppm, p.y*ppm, 15, 15)
