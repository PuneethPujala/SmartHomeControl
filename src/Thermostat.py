from smart_device import SmartDevice

class Thermostat(SmartDevice):

    def __init__(self, name):
        super().__init__(name) 
    
    def set_temperature(self,temp):
        self.temp=temp
        print(f"Ac is set to {self.temp} degrees")
    
    def get_temperature(self):
        return self.temp
    
    def __str__(self):
        return f"{self.name} is currently set to {self.temp} degrees"
    
    
    


    

    