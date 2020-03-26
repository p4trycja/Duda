def setup():
    size(600, 600)
    point(50, 50)
    rectMode(RADIUS)
def draw():
    if mousePressed:
        rect(mouseX, mouseY, 50, 50)
    else:
        line(width, height, mouseX, mouseY)

#2pkt
    
