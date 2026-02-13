from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self): #abstraction doesnot allow implimentation
        pass           
class Car(Vehicle):
    def start(self):
        print("Vehicle is car000")

C=Car()
C.start()

