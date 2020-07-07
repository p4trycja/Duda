def setup():
    global img
    size(600, 600)
    img = loadImage("image.png")
    noFill()
    strokeWeight(20)
    textSize(40)

def draw():
    try:
        image(img, 107, 107, 400, 400) # tylko tą linię trzeba sprawdzić pod kątem błędu, więc tylko ona powinna znaleźć się w try, reszta w else
    except:
        stroke("#FF0000")
        text("BLAD Z PLIKIEM", 155, 65)
    else:
        stroke("#0000FF")
    finally:
        rect(107, 107, 400, 400)
        
#1,5pkt
