from abc import ABC, abstractmethod
import inspect


class Instrument(ABC):              
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def display_info(self):              
        print(f"{self.name} ({self.family})")

   
    @abstractmethod
    def play_sound(self):               
        pass


class Guitar(Instrument):
    def __init__(self, name, family, strings):

        super().__init__(name, family)
        self.strings = strings

    def play_sound(self):                
        print(f"{self.strings} strings go: Strum strum!")


class Tabla(Instrument):
    def __init__(self, name, family, drums):          
        Instrument.__init__(self, name, family)
        self.drums = drums

    def play_sound(self):
         print("(no sound yet)")  


band = [Guitar("Acoustic Guitar", "String", 6), Tabla("Tabla", "Percussion", 2)]   

for instrument in band:
    instrument.display_info()
    instrument.play_sound()

print("The show has not started yet.")
print("Is Instrument abstract?", inspect.isabstract(Instrument))
