def setup():
    global img
    size(600, 600)
    img = loadImage("image.png")

def draw():
    rect(107, 107, 400, 400)
    try:
        strokeWeight(20)
        stroke("#0000FF")
        image(img, 107, 107, 400, 400)
    except:
        strokeWeight(20)
        stroke("#FF0000")
        textSize(40)
        text("BLAD Z PLIKIEM", 155, 65)
