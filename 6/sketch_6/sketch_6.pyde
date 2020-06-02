class Kwadrat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat):
    def sketchPasiasty(self, x, y, paski): 
        Kwadrat.sketch(self, x, y)
        space = self.bok/paski
        _xLinii_ = 0 
        for pasek in range(0, paski):
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
class KolorowyKwadrat(Kwadrat):
    def sketchKolorowy(self, x, y):
        Kwadrat.sketch(self, x, y)
        noStroke()
        colorMode(HSB, 360, 100, 100)                                         
        for  i in range(x):  
            fill(i, 100, 100)
        
def setup():
    size(500, 500)
    n = color(0, 0, 255)
    c = color(255, 0, 0)
    z = color(0, 255, 0)
    
    malyKwadrat = Kwadrat(50.0) 
    malyKwadrat.sketch(200, 300) 
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50, 75)
    
    malyPasiastyKwadrat = PasiastyKwadrat(30.0)
    malyPasiastyKwadrat.sketchPasiasty(300, 300, 5) 
    malyPasiastyKwadrat.sketchPasiasty(100,300, 8) 
    
    malyKolorowyKwadrat = KolorowyKwadrat(70.0)
    malyKolorowyKwadrat.sketchKolorowy(50, 400)
    malyKolorowyKwadrat = KolorowyKwadrat(70.0)
    malyKolorowyKwadrat.sketchKolorowy(200, 400)
    malyKolorowyKwadrat = KolorowyKwadrat(70.0)
    malyKolorowyKwadrat.sketchKolorowy(350, 400)
    
    duzyKolorowyKwadrat = KolorowyKwadrat(150.0)
    duzyKolorowyKwadrat.sketchKolorowy(300, 100)
    
    malyKolorowyKwadrat = KolorowyKwadrat(50.0) 
    malyKolorowyKwadrat.sketchKolorowy(125, 150)
    malyKolorowyKwadrat = KolorowyKwadrat(50.0) 
    malyKolorowyKwadrat.sketchKolorowy(350, 150)
