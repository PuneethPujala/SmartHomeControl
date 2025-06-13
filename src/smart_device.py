from abc import ABC,abstractmethod

class SmartDevice(ABC):

    def __init__(self,name,status):
        self.name=name
        self.status=status

    def __str__(self):
        return f"{self.name} is currently {self.status}"
        
    def turn_on(self):
        self.status = "ON"
        print(f"{self.name} turned ON")

    def turn_off(self):
        self.status = "OFF"
        print(f"{self.name} turned OFF")

    def get_status(self):
        return self.status
