def setup(): 
    size(400, 400) 
    textSize(200)   
    strokeWeight(2) 
    
def draw():  

    clear()
    background(157, 166, 206)

    text("P", width/2-50, height/2)
    k = get(mouseX, mouseY)
    print(hex(k))
    print(keyPressed)
    
    if (k == -1):
        text("P", width/2-50, height/2)
        fill(36, 222, 97)
            
    text("P", width/2-50, height/2)
    fill(255, 255, 255)
    text("D", width/2+50, height/2)
    
    if keyPressed and (k == -1):
        if keyCode == 39:
            fill(255, 255, 255)
            text("P", width/2-50, height/2)
            fill(52, 76, 245)
            text("D", width/2+50, height/2)
      
    if keyPressed:
        if key == "d":
            text("D", width/2+50, height/2)
            fill(52, 76, 245)
        if keyCode == 37:
            fill(36, 222, 97)
            text("P", width/2-50, height/2)
            fill(255, 255, 255)
                    
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
