from abc import ABCMeta, abstractmethod 
class Pet():
    __metaclass__=ABCMeta 
    @abstractmethod 
    def speak(self): 
        super().__init__()
        return 'no sound'
class Cat(Pet): 
    def __init__(self, name):
        self.name = name
    def speak(self): 
        text('meow', random(50, width-70), random(50, height-50))
        return 'meow'
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('woof', random(50, width-70), random(50, height-50))
        return 'woof'
    def gimmePaw(self):
        image(loadImage("lapa.png"), random(50, width-70), random(50, height-100))
    def __add__(self, other): 
        return self.name[0]+ ' i ' + other.name[0]
class Tarantula(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text("^;;^ ", random(50, width-70), random(50, height-50))
        return "^;;^"
    def gimmiePajak(self):
        image(loadImage("pajak.png"), random(50, width-70), random(50, height-100))
    def __sub__(self, other):
        return self.name[0]+ ' minus ' + other.name[0]    
    
def setup():
    size(800, 800)
    textSize(20)
    rex = Dog('Rex') 
    benio = Dog('Benio')
    skrypcik = Cat('Skrypcik') 
    quentino_tarantulino = Tarantula('Quentino Tarantulino') #imie jednego z moich pajakow
    skorpion = Tarantula('Skorpion') #imie kolejnego mojego pajaka
    global list_of_pets
    list_of_pets = [rex, benio, skrypcik, quentino_tarantulino, skorpion]
    print(isinstance(skrypcik, Pet)) 
    print(isinstance(skorpion, Dog))
    print(isinstance(skorpion, Tarantula))
    print(rex+benio)
    print(quentino_tarantulino-skorpion)

def draw():
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak() 
        if isinstance(pet, Dog):
            pet.gimmePaw()
        if isinstance(pet, Tarantula):
            pet.gimmiePajak()
            
# 2 pkt
