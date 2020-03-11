def setup():
    size(600, 600)
    rectMode(CENTER)
    background(255)
    global x
    global y
    global xm
    global ym
    xm = 1
    ym = 1
    x = 50
    y = 300

def draw():
    global x
    global y
    global xm
    global ym
    rect(x, y, 100, 100)
    x = x + xm
    y = y + ym
    
    if(y > height-50):
        fill(255,0,0)
        ym = ym * -1

    if (x > width-50):
        fill(0,255,0)
        xm = xm * -1

    if(y < 50):
        fill(0,0,255)
        ym = ym * -1
       
    if(x == 50):
        exit()
