import random 
add_library('pdf')

def setup():
    global img 
    size(492, 633)
    img = loadImage("aaa.png")
    global img2 
    img2 = loadImage("1.png")
    global img3
    img3 = loadImage("2.png")
    global img4
    img4 = loadImage("3.png")
    
    beginRecord(PDF, "out.pdf")
    
    print(random.random()) 
    print(type(img)) 
    fill(20,255,200)
    
def draw():
    global img
    global img2
    global img3
    global img4
    image(img, 0,0, 492, 633)
    image(img4, 75, 20, 350, 250)

    if keyPressed: #wybór okularów strzałkami, żeby zapisać zdjęcie z okularami należy trzymając strzałkę kliknąć myszką i zamknąć program
        if keyCode == 37:
            image(img2, 93, 195, 300, 200)
        if keyCode == 39:
            image(img3, 93, 195, 300, 200)    
        

def mousePressed():
    endRecord() 
    exit() 
    

    
