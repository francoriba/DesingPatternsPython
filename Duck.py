from abc import ABC, abstractclassmethod

class Duck(ABC):

    def __init__(self, type, color, gender):
        self._type = type
        self._color = color
        self._gender = gender
        
    @property
    def get_type(self):
        return self._type

    @property
    def get_color(self):
        return self._color

    @property
    def get_gender(self):
        return self._gender
    
    @get_type.setter
    def set_type(self, new_type):
        self._type = new_type

    @get_color.setter
    def set_color(self, new_color):
        self._color = new_color

    @get_gender.setter
    def set_gender(self, new_gender):
        self._gender = new_gender

    def quack():
        print("Cuack Cuack")

    def swim():
        print("splash slash")

    @abstractclassmethod
    def display():
        pass

class MallardDuck(Duck):
    def __init_subclass__(self, type, color, gender):
        super().__init__(type, color, gender) #llamada al método __init__() de la clase padre

    def display(self):
        print("Im a Mallard duck")

class RedheadDuck(Duck): 
    def __init_subclass__(self, type, color, gender):
        super().__init__(type, color, gender) 

    def display(self):
        print("Im a ",self.get_type, " duck")

class RubberDuck(Duck): 
    def __init_subclass__(self, type, color, gender):
        super().__init__(type, color, gender) 

    def squeak(self):
        print("squeak squeak squeak")

    def display(self):
        print("Im a ",self.get_type, " duck")


patoRojo = RedheadDuck("Redhead", "Red", "Male")
patoMallard = MallardDuck("Mallard ", "White", "Female")
patoRubber = RubberDuck("Rubber", "Yellow", "Male")


patoRojo.display()
patoRubber.display()
patoRubber.squeak()