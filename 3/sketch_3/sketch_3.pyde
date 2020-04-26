def setup(): 
    size(400, 400) 
    textSize(200)   
    strokeWeight(2)
    global kolor1, kolor2 # tak jest korzystniej dla czytelności - inspiracja na przyszłość
    kolor1 = (36, 222, 97)
    kolor2 = (52, 76, 245)
    global czyD
    czyD = False
    
def draw():  

    clear()
    background(157, 166, 206)
    global czyD

    text("P", width/2-50, height/2)
    k = get(mouseX, mouseY)
    print(hex(k))
    print(keyPressed)
    
    if (k == -1):
        text("P", width/2-50, height/2)
        fill(*kolor1)
            
    text("P", width/2-50, height/2)
    fill(255, 255, 255)
    text("D", width/2+50, height/2)
    
    if keyPressed and (k == -1):
        if keyCode == 39:
            fill(255, 255, 255)
            text("P", width/2-50, height/2)
            fill(*kolor2)
            text("D", width/2+50, height/2)
      
    if keyPressed:
        if key == "d":
            text("D", width/2+50, height/2)
            fill(*kolor2)
            czyD = True
        if keyCode == 37 and czyD:
            fill(*kolor1)
            text("P", width/2-50, height/2)
            fill(255, 255, 255)
    else:
        czyD = False
                    
    text("D", width/2+50, height/2)
    fill(255, 255, 255)        
                   
    s = createShape() 
    s.beginShape() 
    s.fill(208, 76, 245)
    s.stroke(229, 165, 207)
    s.vertex(100, height/3*2) 
    s.vertex(20, height/5*2-80)
    s.vertex(width/4, height/3*2-12)
    s.vertex(width-50, height/3*2+80)
    s.vertex(width-100, height/3*2-20)
    s.endShape(CLOSE)
    shape(s, 25, 25)
    
# P zaznaczało się przy samej strzałce w lewo, ale to było tricky, więc uznaję, poprawiłąm, przeanalizuj rozwiązanie (dwa klawisze nie mogą być policzone jako kliknięte w jednej klatce)
#2pkt
