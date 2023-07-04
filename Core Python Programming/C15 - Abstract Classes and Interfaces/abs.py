#A python program to create a Car abstract class that contains an instance variable, a concrete method and two abstract methods.
#This is an abstract class. Save this code as abs.py
from abc import *
class Car(ABC):
    def __init__(self, regno):
        self.regno = regno
        
    def openTank(self):
        print('Fill the fuel into the tank')
        print('for the car with regno ', self.regno)
        
    @abstractmethod
    def steering(self):
        pass
    
    @abstractmethod
    def braking(self):
        pass