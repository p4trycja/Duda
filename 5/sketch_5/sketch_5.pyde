import random
class Stoper():
    def __init__(self, arg_x, arg_y, arg_r): 
        self.obrot = 0
        self.wcisniety = False 
        self.x = arg_x 
        self.y = arg_y
        self.r = arg_r
    def rysuj(self): 
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+90), PI+ radians(self.obrot+90), PIE) 
        arc(self.x, self.y, self.r, self.r, 0+radians(self.obrot+270), PI+ radians(self.obrot+450), PIE) 
    def obroc(self, stopnie):
        self.obrot += stopnie
    def wcisnij(self): 
        textSize(30)
        text("sekundy: ", 160, 630)
        text(sekundy, 320, 630)
        text("minuty: ", 160, 680)
        text(sekundy/60, 320, 680)
        text("godziny: ", 160, 730)
        text(sekundy/3600, 320, 730)
        textSize(15)
        text("kliknij esc, zeby wyjsc", 170, 790)    
        
def setup():
    frameRate(1)
    size(500, 800)
    global img
    global sekundy
    img = loadImage("abc.png")
    global tarcza 
    tarcza = Stoper(width/2, 350, 400) # miały być utworzone dwa obiekty i taki dobór klasy, żeby ich powielanie miało sens

def mousePressed():
    tarcza.wcisnij()
    noLoop()
    
def keyPressed():
    if keyCode == 27:
        exit()
    
def draw(): 
    background(560)
    textSize(15)
    text("kliknij, zeby zatrzymac", 170, 120)
    textSize(60)
    text("STOPER", 145, 90)
    tarcza.rysuj() 
    global img
    global sekundy
    image(img, 50, 150, 400, 400)
    
    tarcza.obroc(6)
    sekundy = tarcza.obrot/6 - 1
    print(sekundy)
    
# plus do aktywności za kreatywność w sferze wizualnej, szkoda, że w kodzie już nieco mniejsza i opierasz się głównie na kalce moich metod i atrybutów
# 1,5pkt
